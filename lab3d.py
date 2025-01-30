#!/usr/bin/env python3

# Author ID: rfrancisco6

import subprocess

def free_space():
    cmd = "df -h | grep '/$' | awk ' {print $4}'"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())