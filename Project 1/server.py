#!/usr/bin/env python3

import socket

HOST = '10.0.0.1'  # put the ip address of the server here
#HOST = '127.0.0.1'  # put the ip address of the server here
PORT = 65432     

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

                # TODO: append the data with bytes ' from server' and send the concacatenated bytes
                

if __name__ == "__main__":
    main()
