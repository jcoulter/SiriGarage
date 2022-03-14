import socket

# create an datagram socket (single UDP request and response, then close)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect to an address on the internet, that's likely to always be up 
# (the Google primary DNS is a good bet)
sock.connect(("1.1.1.1", 80))
# after connecting, the socket will have the IP in its address
print(sock.getsockname()[0])
#print(sock.gethostname())
# done
sock.close


import os
import time
from datetime import datetime
from flask import Flask, render_template, request
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname() + ".local")

print(hostname)
print(ip_address)
print(socket.getsockname())
