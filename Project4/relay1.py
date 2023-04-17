#!/usr/bin/env python3

import socket
import util

HOST = '10.0.0.11'  # put the ip address of the relay1 (as a TCP server) here
PORT = 20001

# measurements contained in this relay
# TODO replace x1 from the values you obtained from running calculate_fdia.m
measurements = {11: 1.00, 12: 0.00, 13: 0.67, 14: 0.00, \
          21: 1.00, 22: 0.17, 23: 1.63, 24: 0.00}
#measurements = {11: 1.00, 12: 0.00, 13: 0.67, 14: 0.00, \
#          21: 1.00, 22: x1, 23: 1.63, 24: 0.00}


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
