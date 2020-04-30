import socket
import sys
import time
from random import randint
import fileIO
import threading

BYTE_SIZE = 1024
HOST =  '127.0.0.1'
PORT = 5000
PEER_BYTE_DIFFERENTIATOR = b'\x11'
RAN_TIME_START = 1
RAN_TIME_END = 2
REQUEST_STRING = "req"


