#!/usr/bin/env python3

def add(x, y):
    try:
        return int(x) + int(y)
    except:
        return "error: could not add numbers"

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except:
        return "error: could not read file"
