#!/usr/bin/env python3

import socket
import util

HOST = '10.0.0.20'  # put the ip address of the data aggregator here
PORT = 20000

measure_index = [11, 12, 13, 14, \
                 21, 22, 23, 24, \
                 31, 32, 33, 34, \
                 41, 42, 43, 44, \
                 51, 52, 53, 54, \
                 61, 62, 63, 64, \
                 71, 72, 73, 74, \
                 81, 82, 83, 84, \
                 91, 92, 93, 94]

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        input('Prepare to make connection. (Press ENTER to execute s.connect() )')
        s.connect((HOST, PORT))
        input('Prepare to send data. (Press ENTER to execute s.sendall() )')
        # Construct DNP3m request
        req = util.pack_dnp3m_request(measure_index)
        s.sendall(req)
        
        # Expect responses from the Data Aggregator
        res = s.recv(1024)
        # Parsing responses
        all_measure = util.unpack_dnp3m_response(res)
        # Print all measurements
        util.print_measure(all_measure)
        
        input('Prepare to close the connection.(Press ENTER to execute s.close() )')
        s.close()

if __name__ == "__main__":
    main()
