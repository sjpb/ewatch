#!/usr/bin/env python
""" Run a command repeatedly and output differences in output

        Usage:
                ewatch.py command delay
"""

import subprocess, sys, datetime, time

cmd = sys.argv[1]
delay = float(sys.argv[2])
old = (None, None)

while True:
    timestamp = datetime.datetime.now()
    tz = time.strftime("%z", time.gmtime())
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    new = proc.communicate() # stdout, stderr
    if old != new:
        print "-- {timestamp} ({tz}) --".format(timestamp=timestamp, tz=tz)
        print new[0]
        print new[1]
    old = new
    time.sleep(delay)
