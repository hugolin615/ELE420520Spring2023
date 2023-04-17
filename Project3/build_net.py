#!/usr/bin/python
 
 
from mininet.net import Mininet
from mininet.node import Controller, OVSController, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
import os
import os.path

def main():
    setLogLevel('info')

    ### DON't CHANGE as we use default SDN controller
    net = Mininet(controller=Controller, switch=OVSSwitch )
    c1 = net.addController( 'c1', controller=Controller)

    # build a network of the topology mentioned in the instruction

    ## added nodes: switches and hosts
    s1 = net.addSwitch("s1", mac = 11)
    s2 = net.addSwitch("s2", mac = 12)
    s3 = net.addSwitch("s3", mac = 13)
    cc = net.addHost('cc', ip='10.0.0.1')
    da = net.addHost('da', ip='10.0.0.20')
    relay1 = net.addHost('relay1', ip='10.0.0.11')
    relay2 = net.addHost('relay2', ip='10.0.0.12')
    relay3 = net.addHost('relay3', ip='10.0.0.13')
    relay4 = net.addHost('relay4', ip='10.0.0.14')

    ## added links connecting nodes
    net.addLink('s1', 's2')
    net.addLink('s2', 's3')
    net.addLink('cc', 's1')
    net.addLink('da', 's2')
    net.addLink('relay1', 's3')
    net.addLink('relay2', 's3')
    net.addLink('relay3', 's3')
    net.addLink('relay4', 's3')

    net.build()
    net.start()
    
    cc.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Control Center\' &')
    da.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Data Aggregator\' &')
    da.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Data Aggregator\' &')
    relay1.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Relay 1\' &')
    relay2.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Relay 2\' &')
    relay3.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Relay 3\' &')
    relay4.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T \'Relay 4\' &')
    
    CLI(net)

    net.stop()


if __name__ == "__main__":
    main() 
