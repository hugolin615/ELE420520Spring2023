#!/usr/bin/env python3

import socket

SERVER = '10.0.0.1'   # put the ip address of the server
MY_HOST = '10.0.0.2'  # put the ip address of the forward machine
PORT = 65432

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_to_server:
        input('Prepare to make connection. (Press ENTER to execute s.connect() )')
        # TODO: make connection to Server machine; you should expect 1 line of codes
        

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_to_client:
            s_to_client.bind((MY_HOST, PORT)) 
            s_to_client.listen()
            print('Waiting for client to connect.')

            # TODO: using s_to_client to take connections from Client machine
            #    return conn, addr objects; you should expect 1 line of codes
            

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
                
                    # TODO: you should expect 3 lines of codes to do
                    #  1. append bytes from Client machine with ' from forward' and send them to Server machine
                    #  2. receive network packets from Server machine
                    #  3. append bytes from Server machine with ' from forward' and send them to Client machine



if __name__ == "__main__":
    main()

    # CHANGE: providing the socket to Server
