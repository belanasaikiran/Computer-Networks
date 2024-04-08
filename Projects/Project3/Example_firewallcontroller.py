# Firewall controller
#
# Based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.tcp import tcp
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)


  def do_firewall (self, event):
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.

    # The code in here will be executed for every packet.
    def flood (duration = 30):
      """ Floods the packet """
      if not isinstance(duration, tuple):
        duration = (duration,duration)
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet)
      msg.idle_timeout = duration[0]
      msg.hard_timeout = duration[1]
      msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
      msg.buffer_id = event.ofp.buffer_id
      self.connection.send(msg)

    def drop (duration = 30):
      """
      Drops this packet and optionally installs a flow to continue
      dropping similar ones for a while
      """
      if not isinstance(duration, tuple):
        duration = (duration,duration)
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet)
      msg.idle_timeout = duration[0]
      msg.hard_timeout = duration[1]
      msg.actions = []
      msg.buffer_id = event.ofp.buffer_id
      self.connection.send(msg)

    print "---------new------------"
    print packet
    print packet_in
    print "---------parse------------"
    print isinstance(packet, ethernet), packet.find('arp'), packet.find('ipv4'), packet.find('tcp')

    if packet.find('arp') or packet.find("ipv4") and packet.find("tcp"):
      print "---FLOOD"
      flood()
    else:
      drop()
      print "---DROP"
    
  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    self.do_firewall(event)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
