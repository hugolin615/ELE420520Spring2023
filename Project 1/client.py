
#!/usr/bin/env python3

import socket

HOST = '10.0.0.2'  # put the ip address of the forward here
PORT = 65432     

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        input('Prepare to make connection. (Press ENTER to execute s.connect() )')
        # TODO: connect to the Forward machine; you should expect one line of python codes
        

        input('Prepare to send data. (Press ENTER to execute s.sendall() )')
        # TODO: send the bytes 'Hello from client' to the Forward machine;
        #  you should expect 2~3 line of python codes
        

        # DON't change: receive the data and print out the received data
        data = s.recv(1024)

        print('Received', repr(data))
        input('Prepare to close the connection.(Press ENTER to execute s.close() )')
        s.close()

if __name__ == "__main__":
    main()
