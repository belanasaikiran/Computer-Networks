# Final Skeleton
#
# Hints:
#
# To check the source and destination of an IP packet, you can use
# the header information... For example:
#
# ip_header = packet.find('ipv4')
#
# if ip_header.srcip == "1.1.1.1":
#   print "Packet is from 1.1.1.1"
#
# Important Note: the "is" comparison DOES NOT work for IP address
# comparisons in this way. You must use ==.
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
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

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. 
    #   - port_on_switch: represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet.
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    # You should use these to determine where a packet came from. To figure out where a packet 
    # is going, you can use the IP header information.msg
    
    msg = of.ofp_flow_mod()
    msg.idle_timeout = 30 #set Idle Timeout
    msg.hard_timeout = 30 #Set Hard Timeout
    msg.match = of.ofp_match.from_packet(packet)
    msg.data = packet_in


    #Let's set packet type boolean variables
    ip = packet.find('ipv4') 
    icmp = packet.find('icmp') 


    # Handle cases where no IP packet is detected
    if ip == None: # Check if there is no IPv4 packet in the incoming data
        msgAction = of.ofp_action_output(port = of.OFPP_FLOOD)  # Create an action to flood the packet
        msg.actions.append(msgAction)  # Append the flooding action to the action list of the message
        #print('non IP, flooded')

    else:
        # Handling when the packet contains IP data
        if switch_id == 1:  # If the packet is being handled by switch 1
            if port_on_switch == 1:  # If the packet comes from port 1 (from h1)
                msgAction = of.ofp_action_output(port=2)  # Create an action to forward the packet to port 2 (to s4)
                msg.actions.append(msgAction)  # Append the forwarding action to the message
                print("packet sent to S4")
            elif port_on_switch == 2:  # If the packet comes from port 2 (from s4)
                msgAction = of.ofp_action_output(port=1)  # Create an action to forward the packet to port 1 (back to h1)
                msg.actions.append(msgAction)
                print("Packet sent to h1")

        elif switch_id == 2:  # If the packet is being handled by switch 2
            if port_on_switch == 1:  # If the packet comes from port 1 (from h2)
                msgAction = of.ofp_action_output(port=2)  # Create an action to forward the packet to port 2 (to s4)
                msg.actions.append(msgAction)
                print("Packet sent to s4")
            elif port_on_switch == 2:  # If the packet comes from port 2 (from s4)
                msgAction = of.ofp_action_output(port=1)  # Create an action to forward the packet to port 1 (back to h2)
                msg.actions.append(msgAction)
                print("Packet sent to h2")

        elif switch_id == 3:  # If the packet is being handled by switch 3
            if port_on_switch == 1:  # If the packet comes from port 1 (from h3)
                msgAction = of.ofp_action_output(port=2)  # Create an action to forward the packet to port 2 (to s4)
                msg.actions.append(msgAction)
                print("Packet send to s4")
            elif port_on_switch == 2:  # If the packet comes from port 2 (from s4)
                msgAction = of.ofp_action_output(port=1)  # Create an action to forward the packet to port 1 (back to h3)
                msg.actions.append(msgAction)
                print("Packet sent to h3")

        elif switch_id == 5:  # If the packet is being handled by switch 5
            if port_on_switch == 1:  # If the packet comes from port 1 (from h5)
                msgAction = of.ofp_action_output(port=2)  # Create an action to forward the packet to port 2 (to s4)
                msg.actions.append(msgAction)
                print("Packet sent to s5")
            elif port_on_switch == 2:  # If the packet comes from port 2 (from s4)
                msgAction = of.ofp_action_output(port=1)  # Create an action to forward the packet to port 1 (back to h5)
                msg.actions.append(msgAction)
                print("Packet sent to h5")


        
        elif switch_id == 4:  # Check if the current switch ID is 4.
            # If packet is from h4 - untrusted host, drop it. We block all the traffic coming from h4 (untrusted host) to our server h5
            if port_on_switch == 1:  # Check if the packet came from port 1.
                # Check if the packet is ICMP and drop it if coming from h4 (untrusted host). We can test it with the `pingall` command in mininet environment.
                if icmp != None:
                    self.connection.send(msg)
                    print("ICMP packet from h4 dropped")
                    return
                # Drop IP packets directed to h5 from h4.
                elif ip.dstip == '10.5.5.50':
                    self.connection.send(msg)
                    print("ICMP packet from h4 to h5 dropped")
                    return
                # Forward IP packets destined for h1.
                elif ip.dstip == '10.1.1.10':
                    msgAction = of.ofp_action_output(port=2)
                    msg.actions.append(msgAction)
                    print('Sent to Host 1')
                # Forward IP packets destined for h2.
                elif ip.dstip == '10.2.2.20':
                    msgAction = of.ofp_action_output(port=3)
                    msg.actions.append(msgAction)
                    print("sent to host 2")
                # Forward IP packets destined for h3.
                elif ip.dstip == '10.3.3.30':
                    msgAction = of.ofp_action_output(port=4)
                    msg.actions.append(msgAction)
                    print("sent to host 3")
            else:  # If the packet came from any port other than 1.
                # Forward packets with a specific destination IP to h4.
                if ip.dstip == '123.45.67.89':
                    msgAction = of.ofp_action_output(port = 1)
                    msg.actions.append(msgAction)
                    print("Sent to host 4")
                # Forward packets destined for h1.
                elif ip.dstip == '10.1.1.10':
                    msgAction = of.ofp_action_output(port = 2)
                    msg.actions.append(msgAction)
                    print("Sent to host 1")
                # Forward packets destined for h2.
                elif ip.dstip == '10.2.2.20':
                    msgAction = of.ofp_action_output(port = 3)
                    msg.actions.append(msgAction)
                    print("Sent to host 2")
                # Forward packets destined for h3.
                elif ip.dstip == '10.3.3.30':
                    msgAction = of.ofp_action_output(port = 4)
                    msg.actions.append(msgAction)
                    print("Sent to host 3")
                # Forward packets destined for h5.
                elif ip.dstip == '10.5.5.50':
                    msgAction = of.ofp_action_output(port = 5)
                    msg.actions.append(msgAction)
                    print("Sent to host 5")


    self.connection.send(msg)
    return                



    #f print("Example code.")

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
