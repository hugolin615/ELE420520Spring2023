
#!/usr/bin/env python3

import socket

#HOST = '127.0.0.1'  # The server's hostname or IP address
HOST = '10.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        input('Prepare to make connection. (Press ENTER to execute s.connect() )')
        s.connect((HOST, PORT))
        input('Prepare to send data. (Press ENTER to execute s.sendall() )')
        s.sendall(b'Hello, world')
        data = s.recv(1024)

        print('Received', repr(data))
        input('Prepare to close the connection.(Press ENTER to execute s.close() )')
        s.close()

if __name__ == "__main__":
    main()
