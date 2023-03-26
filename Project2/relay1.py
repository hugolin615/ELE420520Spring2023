#!/usr/bin/env python3

import socket
import util

HOST = '10.0.0.11'  # put the ip address of the relay1 (as a TCP server) here
PORT = 20001

# measurements contained in this relay
measurements = {11: 1.00, 12: 0.00, 13: 71.95, 14: 24.07, \
          21: 1.00, 22: 9.67, 23: 163.00, 24: 14.46}

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
