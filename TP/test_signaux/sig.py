#!/usr/bin/python3
import signal as sig
from time import sleep
import sys, os

def signal_handler(s, frame):
    print("réception du signal ", sig.Signals(s).name )
    if sig.Signals(s) == sig.SIGINT:
        sys.exit(0)
        

sig.signal(sig.SIGINT, signal_handler)
sig.signal(sig.SIGQUIT, signal_handler)

x=1
while True:
    print("pid=", os.getpid(), x)
    sleep(.5)
    x += 1
