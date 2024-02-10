# This code explains the implementation of 4 hosts and 1 switch

from mininet.net import Mininet # import Mininet
# from mininet.node import Controller # import controller if you are using default controller or use RemoteController if it is not available.
from mininet.node import RemoteController # In my case, I'm using the remote controller called ovs-testcontroller. It's a separate pacakge
from mininet.cli import CLI
from mininet.log import setLogLevel, info #for system logs - print functions here

def emptyNet():

    """
    Create an empty network and add nodes to it.
    """

    # net = Mininet(controller=Controller) #use this for default controller
    net = Mininet(controller=RemoteController)

    info("*** Adding Controller\n")
    net.addController('c0')

    info('*** Adding Hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    h4 = net.addHost('h4', ip='10.0.0.4')


    info('*** Adding Switch \n')
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    net.addLink(h1,s1)
    net.addLink(h2,s1)
    net.addLink(h3,s1)
    net.addLink(h4,s1)


    info('*** Starting Network\n')
    net.start()


    info('*** Running CLI\n')
    CLI(net)

    info('** stopping network')
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()




# NOTE: Reference used for remote controller: https://stackoverflow.com/questions/26794816/why-mininet-default-controller-always-work-in-loop-back-interface-127-0-0-1
    # You can also use https://mininet.org/blog/2013/06/03/automating-controller-startup/ when using POX controller