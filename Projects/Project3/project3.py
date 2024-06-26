#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):

    # Create 5 switches.
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')
    s5 = self.addSwitch('s5')

    #assign hosts to the switches
    h1 = self.addHost('h1',mac='00:00:00:00:00:01', ip='10.1.1.10/24', defaultRoute='h1-eth0') #Floor 1
    h2 = self.addHost('h2',mac='00:00:00:00:00:02', ip='10.2.2.20/24', defaultRoute='h2-eth0') #Floor 2
    h3 = self.addHost('h3',mac='00:00:00:00:00:03', ip='10.3.3.30/24', defaultRoute='h3-eth0') #Floor 3    
    h4 = self.addHost('h4',mac='00:00:00:00:00:04', ip='123.45.67.89/24', defaultRoute='h4-eth0') # Untrusted Host
    h5 = self.addHost('h5',mac='00:00:00:00:00:05', ip='10.5.5.50/24', defaultRoute='h5-eth0') # Our Server


    #Link hosts to the Switches
    self.addLink(h1,s1,port1=0, port2=1)
    self.addLink(h2,s2,port1=0, port2=1)
    self.addLink(h3,s3,port1=0, port2=1)
    self.addLink(h4,s4,port1=0, port2=1)
    self.addLink(h5,s5,port1=0, port2=1)

    #Linking the switches to each other as mentioned in the given figure
    self.addLink(s1,s4,port1=2, port2=2)
    self.addLink(s2,s4,port1=2, port2=3)
    self.addLink(s3,s4,port1=2, port2=4)
    self.addLink(s5,s4,port1=2, port2=5)


def configure():
  topo = final_topo()
  # net = Mininet(topo=topo, controller=RemoteController('c0', ip='127.0.0.1', protocol='tcp', port=6633)) #ideal way of implementation since the pox is running at port `6633`.
  net = Mininet(topo=topo, controller=RemoteController) # I use this since the command `dpctl dump-flows` works with this mode only. Could be the pox controller's issue ?
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
