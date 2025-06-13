#!/usr/bin/env python3

def read_file_string(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_file_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def append_file_string(filename, string):
    with open(filename, 'a') as f:
        f.write(string)

def write_file_list(filename, list_data):
    with open(filename, 'w') as f:
        for item in list_data:
            f.write(item + '\n')

def copy_file_add_line_numbers(source, target):
    with open(source, 'r') as src, open(target, 'w') as tgt:
        for i, line in enumerate(src, 1):
            tgt.write(f"{i}:{line}")
