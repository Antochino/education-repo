#!/usr/bin/env python3

# external modules
import sys
import os
import subprocess
import paramiko
import time

# read file
f = open('python.txt')
line = f.readline()

while line:

    print (line)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #filename = '/home/a.ilichev/.ssh/id_rsa' # file host_key

    #privkey = paramiko.RSAKey.from_private_key_file(filename)


    ssh.connect(hostname = line) # connection
    #stdin, stdout, stderr = ssh.exec_command('ls -l')

#if not stderr.readlines(): # cheacking
    # read output
    #res = stdout.readlines()
    #print (res, sep = '\n')
    #sys.stdout.flush()

    ssh.close()

    line = f.readline()

    f.close()
