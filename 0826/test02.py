'''
Created on 2017年8月26日

@author: Lin Yu
'''
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS err: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Inexpected error:", sys.exc_info()[0])
    raise