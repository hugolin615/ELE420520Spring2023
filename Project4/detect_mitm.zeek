
global DATA_AGG_IP: addr = 10.0.0.20;

# dictionary-like data structure to store measurements received by relays
global read_from_relays : table[count] of double = {
    [22] = 0.00, [32] = 0.00, [42] = 0.00, [52] = 0.00, [62] = 0.00, [72] = 0.00, [82] = 0.00, [92] = 0.00, 
    [13] = 0.00, [23] = 0.00, [33] = 0.00, [43] = 0.00, [53] = 0.00, [63] = 0.00, [73] = 0.00, [83] = 0.00, [93] = 0.00, 
};
global read_from_relays_count : count = 0;

# dictionary-like data structure to store measurements sent to control center
global read_from_da : table[count] of double = {
    [22] = 0.00, [32] = 0.00, [42] = 0.00, [52] = 0.00, [62] = 0.00, [72] = 0.00, [82] = 0.00, [92] = 0.00, 
    [13] = 0.00, [23] = 0.00, [33] = 0.00, [43] = 0.00, [53] = 0.00, [63] = 0.00, [73] = 0.00, [83] = 0.00, [93] = 0.00, 
};
global read_from_da_count : count = 0;

# By making this variable to T, you can let zeek to print some measurements from different event handlers
global DEBUG : bool = F;

# Note that here we don't use the Zeek's logging framework; just a simpley log file for our experiment
global dnp3m_log = open("dnp3m.log");

function table_equal(t1: table[count] of double, t2: table[count] of double) : bool
    {
    for (i, m in t1)
        if ( !(i in t2) )
            return F;
        else
            if ( t2[i] != m)
                return F;
    return T;
    }

event zeek_init()
    {
    if (DEBUG)
        print |read_from_da|;
    }

event zeek_done()
    {
    print dnp3m_log, read_from_relays;
    print dnp3m_log, read_from_da;
    close(dnp3m_log);
    }
event dnp3m::request(c: connection, is_orig: bool, index: vector of count)
    {
    if (DEBUG)
        print "dnp3m request", c$id, is_orig, index;
    }

event dnp3m::response(c: connection, is_orig: bool)
    {
    if (DEBUG)
        print "dnp3m response", c$id, is_orig;
    }

event dnp3m::data(c: connection, is_orig: bool, index: count, measure: double)
    {
    if (DEBUG)
        print "dnp3m response data", c$id, is_orig, index, measure;

    if (c$id$orig_h == DATA_AGG_IP)
        {
        if (index in read_from_relays)
            {
            # TODO
            # this if branch corresponds to packets from relays; store "measure" in the appropriate table with the "index"
            read_from_  [ ] = TODO;
            
            read_from_relays_count = read_from_relays_count + 1;
            }
        }
    
    if (c$id$resp_h == DATA_AGG_IP)
        {
        if (index in read_from_da)
            {
            # TODO
            # this if branch corresponds to packets sent to control center; store "measure" in the appropriate table with the "index"
            read_from_  [ ] = TODO;

            read_from_da_count = read_from_da_count + 1;
            }
        }
    
    # I use a very naive way to determine when to compare measurements just for this experiment
    #  when zeek observs that the data_aggregator sends all the measurements, it will compare the measurements
    if (read_from_da_count == |read_from_da|)
        {
        if (read_from_da_count != read_from_relays_count)
            print dnp3m_log, "ERROR on parsing";
    
        if( !table_equal(read_from_relays, read_from_da))
            print dnp3m_log, "ALERT: data collected from relays are not consistent with the data sent to the control center";
        
        read_from_da_count = 0;
        read_from_relays_count = 0;
        }
    }
