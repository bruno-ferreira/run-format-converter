#!/usr/bin/env python
''' docstring '''

import argparse

from xml.etree import ElementTree as ET

# create a class that reads any xml format
# pwx
# gpx
# etc

def pwx_reader(a_file):
    '''docstring'''
    tree = ET.parse(a_file)
    root = tree.getroot()
    print root

def main():
    '''docstring'''
    parser = argparse.ArgumentParser(description='Converts run files formats')

    parser.add_argument('--file', help='run file that will be converted')
    parser.add_argument('--format', help='output format of run file')

    args = parser.parse_args()

    print args

if __name__ == '__main__':
    main()
