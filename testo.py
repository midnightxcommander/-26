#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:50:41 2020

@author: btabaczynski
"""

import os
import datetime


changes = '/home/pi/watchfiles/changes.txt'
exit_file = '/home/pi/watchfiles/exit.now'
config_file = '/home/pi/watchfiles/config.ini'

def prettifyDate(d):
    #TODO - Reformat datetime object ind_date to fmtdDate 
    d = d # String of `ls` output 
    lsfmt = datetime.datetime.strftime("%b %d %I:%M")    # Format of `ls` output
    fmt = datetime.datetime.strftime("%Y-%m%d %I%:M:%S") # Format we want
    ind_date = datetime.datetime.strptime()              # `ls` string-to-date
    fmtdDate = datetime.datetime.strptime()              # 
    return fmtdDate


def getWatchfiles(changes, exit_file, config_file):
    changes = changes
    changes = os.system(f'ls -l {changes}')
    # open this file in this function while = True -> append config_file_timestamp from prettifyDate(d) to changes.txt
    print(changes)
    exit_file = exit_file
    exit_file = os.system(f'ls -l {exit_file}')
    print(exit_file)
    config_file = config_file
    config_file_date = os.system(f"ls -l {config_file} | cut -d ' ' -f 5-7")   # File date ` | prettifyDate(config_file_date)`
    config_file_actual = os.system(f"ls -l {config_file} | awk '{print $NF}'") # The actual file name
    print(type(config_file))
    

configDate, exitFile, changeFile = getWatchfiles(changes, exit_file, config_file)
