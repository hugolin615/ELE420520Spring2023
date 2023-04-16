#!/usr/bin/env python3

import socket
import util

HOST = '10.0.0.13'  # put the ip address of the relay3 (as a TCP server)
PORT = 20003

# measurements contained in this relay
# TODO replace x4 and x5 from the values you obtained from running calculate_fdia.m
measurements = {51: 1.00, 52: -0.07, 53: -0.90, 54: 0.00, \
          61: 1.00, 62: 0.04, 63: 0.00, 64: 0.00}
#measurements = {51: 1.00, 52: x4, 53: -0.90, 54: 0.00, \
#          61: 1.00, 62: x5, 63: 0.00, 64: 0.00}


def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT)) 
        s.listen()
        print('Waiting for client to connect.')

        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print('Waiting for data to receive.')
                if not data:
                    print('An packet without payload is received, end the connection.')
                    break
                else:
                    print('Receiving data')
                    req_indices = util.unpack_dnp3m_request(data)
                    response = util.pack_dnp3m_response(req_indices, measurements)
                   
                conn.sendall(response)


if __name__ == "__main__":
    main()
