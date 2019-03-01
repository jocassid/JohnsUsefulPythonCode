#!/usr/bin/env python3

from argparse import ArgumentParser
from datetime import datetime
from logging import getLogger
from os import system, walk
from os.path import exists, getmtime, isdir, isfile, join 
from time import sleep
from sys import stderr


logger = getLogger(__name__)


class IfItMovesShootIt(object):
    
    def __init__(self, monitor_items, command, number_recent_files=10):
        self.command = command
        self.number_recent_files = number_recent_files
        self.recent_files = []
        
        self.last_update = datetime.now().timestamp()
        self.scan_start = None
        
        self.files = []
        self.dirs = []
        for path in monitor_items:
            if not exists(path):
                print("{} not found".format(path), file=stderr)
                continue
                
            if isdir(path):
                self.dirs.append(path)
                continue
            
            self.files.append(path)
            
    def add_recent_file(self, file_path):
        while len(self.recent_files) > self.number_recent_files + 1:
            self.recent_files.pop(0)
        self.recent_files.append(file_path)

    def files_modified(self, file_list):
        for a_file in file_list:
            mtime = getmtime(a_file)
            if mtime > self.last_update:
                self.last_update = mtime
                self.add_recent_file(a_file)
                return True
        return False
                
    def dirs_modified(self):
        for a_dir in self.dirs:
            # TODO: find a way to leverage scandir function available in 
            # more recent versions of Python
            for root, dirs, files in walk(a_dir):
                for item in dirs + files:
                    path = join(root, item)
                    mtime = getmtime(path)
                    if mtime > self.last_update:
                        self.last_update = mtime
                        self.add_recent_file(path)
                        return True
        return False

    def report_scan_elapsed(self):
        elapsed = datetime.now() - self.scan_start
        logger.debug("scan took {}".format(elapsed))

    def run_command(self):
        self.report_scan_elapsed()
        logger.debug('run {}'.format(self.command))
        system(self.command)
    
    def monitor_loop(self):
        for i in range(100):
            
            sleep(5)
            
            self.scan_start = datetime.now()
            
            if self.files_modified(self.recent_files):
                self.run_command()
                continue
            
            if self.files_modified(self.files):
                self.run_command()
                continue
                
            if self.dirs_modified():
                self.run_command()
                continue
                
            self.report_scan_elapsed()
            
     
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
    #main(parser.parse_args())
    args = parser.parse_args()
    
    iimsi = IfItMovesShootIt(args.monitor, args.command)
    iimsi.monitor_loop()
    

    