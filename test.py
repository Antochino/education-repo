#!/usr/bin/env python3
import os
import subprocess
#a1 = open("test.txt" , "r")
#x = 2
#data = a1.readlines(1)
#print (x)
#print (data)
#a1.close()
#x = 1
#a = 1
#while x<=10:
#read = open("test.txt", "r")
#data = read.read()
#print (data)
#read.close()
#x++
#a++
#read = open("test.txt", "r")
#x = 0
#for line in read:
#       print (line)
#read.close()
#test = subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL)
#print(test.returncode)
#os.system("ping 8.8.8.8")


# -*- coding: utf-8 -*-
f = open('python.txt')
line = f.readline()
while line:
    print (line),
    a = "df -h"
    b = "ssh " + line + a
    os.system(b)
    line = f.readline()
f.close()

# -*- coding: utf-8 -*-
#f = open('python.txt')
#for line in f.readlines():
#    print (line),
