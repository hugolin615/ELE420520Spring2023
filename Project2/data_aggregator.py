#!/usr/bin/env python3

import socket
import errno
from socket import error as socket_error
import util

MY_HOST = '10.0.0.20'
RELAY_IPs = ['10.0.0.11', '10.0.0.12', '10.0.0.13', '10.0.0.14']
PORT = 20000

def main():

    # create four different sockets to connect each relay
    s_to_relays = []
    for i in range(len(RELAY_IPs)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_to_relays.append(s)
    
    print('Make connection to four relays.')
    active_relays = []
    for i in range(len(RELAY_IPs)):
        try:
            s_to_relays[i].connect((RELAY_IPs[i], PORT + i + 1))
        except socket_error as serr:
            print(serr)
            s_to_relays[i].close
            continue
        active_relays.append(i+1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_to_controlcenter:
        s_to_controlcenter.bind((MY_HOST, PORT)) 
        s_to_controlcenter.listen()
        print('Waiting for control center to connect.')

        conn, addr = s_to_controlcenter.accept()

        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print('Waiting for data to receive.')
                if not data:
                    print('An packet without payload is received, end the connection.')
                    break
                else:
                    print('Receiving data from a control center.')
                    list_of_indices = util.unpack_dnp3m_request(data)
                    
                    # initialize storage to store indices
                    relay_indices = {}
                    for i in active_relays:
                        relay_indices[i] = []
                    # grouping indices so that we know which relay to send the request
                    for i in list_of_indices:
                        relay_num = util.index_to_relay(i)
                        if relay_num in relay_indices:
                            relay_indices[relay_num].append(i)
                   
                    relay_measure = {}
                    for key in relay_indices.keys():
                        cur_relay_socket = s_to_relays[key - 1]
                        cur_req = util.pack_dnp3m_request(relay_indices[key])
                        cur_relay_socket.sendall(cur_req)
                        data = cur_relay_socket.recv(1024)
                        relay_measure.update(util.unpack_dnp3m_response(data))
                    aggregate_res = util.pack_dnp3m_response(list_of_indices, relay_measure)    
                    conn.sendall(aggregate_res)

if __name__ == "__main__":
    main()
