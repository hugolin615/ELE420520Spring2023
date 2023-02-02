#!/usr/bin/env python3

import socket

#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
HOST = '10.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

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
                    print('Receiving data from a client.')
                conn.sendall(data)

if __name__ == "__main__":
    main()
