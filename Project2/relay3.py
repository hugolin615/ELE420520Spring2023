#!/usr/bin/env python3

import socket
import util

HOST = '10.0.0.13'  # put the ip address of the relay3 (as a TCP server)
PORT = 20003

# measurements contained in this relay
measurements = {51: 0.98, 52: -4.02, 53: -90, 54: -30, \
          61: 1.01, 62: 1.93, 63: 0.00, 64: 0.00}

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
