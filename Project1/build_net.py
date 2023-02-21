#!/usr/bin/python
 
 
from mininet.net import Mininet
from mininet.node import Controller, OVSController, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
import os
import os.path

def main():
    setLogLevel('info')

    ### DON't CHANGE as we use default SDN controller
    net = Mininet(controller=Controller, switch=OVSSwitch )
    c1 = net.addController( 'c1', controller=Controller)

    # build a network of the following topology
    #   server---s1---s2---s3---client   
    #                  |
    #                forward

    ## added nodes: switches and hosts
    s1 = net.addSwitch("s1", mac = 11)
    s2 = net.addSwitch("s2", mac = 12)
    s3 = net.addSwitch("s3", mac = 13)
    server = net.addHost('server', ip='10.0.0.1')
    forward = net.addHost('forward', ip='10.0.0.2')
    client = net.addHost('client', ip='10.0.0.3')

    ## added links connecting nodes
    net.addLink('s1', 's2')
    net.addLink('s2', 's3')
    net.addLink('server', 's1')
    net.addLink('forward', 's2')
    net.addLink('client', 's3')

    net.build()
    net.start()

    server.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T server &')
    forward.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T forward &')
    forward.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T forward &')
    client.cmd('xterm -xrm \'XTerm.vt100.allowTitleOps: false\' -T client &')
    CLI(net)
    #CLI(net, script=init_script)

    net.stop()


if __name__ == "__main__":
    main() 
