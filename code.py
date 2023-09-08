with open('http_access_log') as f:
    [print(line) for line in f.readlines()]


theFile = open('http_access_log','r')
FILE = theFile.readlines()
theFile.close()
printList = []
for line in FILE:
    if ('TestName' in line) or ('Totals' in line):
         printList.append(line)


import re
import csv
import collections


def log_file_reader(http_access_log):
    
    # Get all IP addresses from the log file
    with open(http_access_log) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex, log)
        return ip_list
    

log_file = open(filename, "r+")
for row in log_file:
    print(row)
    regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_list = re.findall(regex, row)
    print()
    return ip_list
pass
