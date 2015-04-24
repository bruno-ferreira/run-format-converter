#!/usr/bin/env python
''' docstring '''

import argparse
import os
from xml.etree import ElementTree as ET

# create a class that opens and reads any xml format
# pwx
# gpx
# etc


class openXMLFile(object):
    '''docstring'''
    def open():
        tree = ET.parse(self)
        root = tree.getroot()


def pwx_reader(a_file):
    '''docstring'''
    a_file = os.path.abspath(a_file)
    tree = ET.parse(a_file)
    root = tree.getroot()
    print root
    print root.tag  # main tag
    print root.attrib  # main attribute
    for child in root:
        print child.tag, child.attrib


def main():
    '''docstring'''
    # parser = argparse.ArgumentParser(description='Converts run files formats')
    #
    # parser.add_argument('-f', '--file', help='run file that will be converted')
    # parser.add_argument('-t', '--type', help='output type of run file')
    #
    # args = parser.parse_args()
    #
    # print args
    # pwx_reader(args['file'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts run files formats')

    parser.add_argument('-f', '--file', help='run file that will be converted')
    parser.add_argument('-t', '--type', help='output type of run file')

    args = vars(parser.parse_args())

#    print args
    pwx_reader(args['file'])
