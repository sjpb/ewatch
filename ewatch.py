#!/usr/bin/env python
""" Run a command repeatedly and output differences in output

        Usage:
            ewatch.py [options] command
        where options are:
            -n seconds: Update interval, default 2
            -i pattern: Ignore changes matching given regex
"""
from __future__ import print_function
import subprocess, sys, datetime, time, re

def main():
    # parse cli:
    options = {'-d':'2', '-i':None} # defaults
    cmd = sys.argv[-1]
    options.update(zip(*[iter(sys.argv[1:-1])]*2))
    delay = float(options['-d'])
    pattern = options['-i']
    
    old = ['', ''] # stdout, stderr
    while True:
        timestamp = datetime.datetime.now().isoformat()
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        new = [s or '' for s in proc.communicate()] # stdout, stderr
        new_clean = [re.sub(pattern, '', s) for s in new] if pattern else new
        if old != new_clean:
            print("[{timestamp}]".format(timestamp=timestamp))
            print(new[0]) # NB not new_clean!
            if new[1]:
                print('stderr:', new[1])
        old = new_clean
        time.sleep(delay)

if __name__ == '__main__':
    main()