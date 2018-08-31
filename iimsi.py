#!/usr/bin/env python3

from argparse import ArgumentParser
from datetime import datetime
from os.path import getmtime, isdir, isfile
from time import sleep


class IfItMovesShootIt(object):
    pass


def run_command(command):
    print("command gets run here!")

def main(args):
    last_update = datetime.now().timestamp()
    command = args.command
    
    files = []
    directories = []
    for item in args.monitor:
        if isdir(item):
            directories.append(item)
            continue
        files.append(item)
        
    print('files', files)
    print('directories', directories)
        
    for i in range(100):
        sleep(5)
        
        bail = False
        for a_file in files:
            mtime = getmtime(a_file)
            if mtime <= last_update:
                continue
            last_update = mtime
            run_command(command)
            bail = True
            
        if bail:
            continue

        for a_dir in directories:
            pass
        
      
    # Travis demo of scandir (faster than os.walk and pulls back metadata)
    # https://github.com/deeppunster/Walk_vs_Scan/blob/master/NewWalkVsScan.py
    


if __name__ == '__main__':

    parser = ArgumentParser(description="Monitor files or directories for changes and then run a command")
    parser.add_argument(
        '-m', '--monitor', 
        metavar='FILE', 
        nargs='+',
        required=True,
        help="files/directories to monitor")
    parser.add_argument(
        '-c', '--command',
        required=True,
        help="command to run and its arguments (put in quotes)")
    main(parser.parse_args())
    

    