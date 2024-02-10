""" Custom Topology:

Two directly connected switched plus a host for each switch:

    host --- switch --- swithc --- host


Adding the `topos` dict with a key-value pair to generate our newly defined topology enables one to pass in `--topo=mytopo` from the command lin.
"""

from mininet.topo import Topo

class MyTopo ( Topo ):
    "Simple Topology Example."

    def build(self):
        "create a custom topo"


        # adding hosts and switches
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addSwitch('s3')
        rightSwitch = self.addSwitch('s4')

        # add links
        self.addLink(leftHost, leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightSwitch, rightHost)


topos = { 'mytopo': (lambda: MyTopo())}