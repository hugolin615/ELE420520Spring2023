#!/usr/bin/env python3

import socket
import util

HOST = '10.0.0.14'  # put the ip address of the relay4 (as a TCP server)
PORT = 20004

# measurements contained in this relay
measurements = {71: 0.99, 72: 0.62, 73: -100.00, 74: -35.00, \
          81: 1.00, 82: 3.80, 83: 0.00, 84: 0.00, \
          91: 0.96, 92: -4.35, 93: 0.00, 94: 0.00}

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
