__author__ = 'alexander'
import time
import logging
import fileinput
import math

infile = open('C:\\install.log', 'r')
outfile = open('C:\\install.log', 'w')

for log in infile:
    print(log, end='')

print(time.strftime('%A %b/%d/%Y', time.localtime()))
print(math.trunc(2.33))