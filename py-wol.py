import argparse
import sys
import struct
import socket

parser = argparse.ArgumentParser(description='Very Very Very Simple Python Wake On Lan')
parser.add_argument('-m','--mac', help='Mac Address to Wake Up', required=True)
args = parser.parse_args()

# Configuration variables
broadcast = ['192.168.160.255']
wol_port = 9

def WakeOnLan(ethernet_address):

    # Construct 6 byte hardware address
    add_oct = ethernet_address.split(':')
    print (add_oct)
    print (len(add_oct))
    hwa = struct.pack('BBBBBB', int(add_oct[0],16),
        int(add_oct[1],16),
        int(add_oct[2],16),
        int(add_oct[3],16),
        int(add_oct[4],16),
        int(add_oct[5],16))
    # Build magic packet
    msg = b'\xff' * 6 + hwa * 16
    # Send packet to broadcast address using UDP port 9
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    for i in broadcast:
        soc.sendto(msg,(i,wol_port))
    soc.close()

WakeOnLan (args.mac)
