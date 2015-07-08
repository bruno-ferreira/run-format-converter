#!/usr/bin/env python
"""docstring"""

import argparse
import os
from xml.etree import ElementTree as ET

# create a class that opens and reads any xml format
# pwx
# gpx
# etc
# json


class OpenXMLFile(object):
    """docstring"""
    def open(self):
        tree = ET.parse(self)
        root = tree.getroot()


def pwx_reader(a_file):
    """docstring"""
    a_file = os.path.abspath(a_file)
    tree = ET.parse(a_file)
    root = tree.getroot()
    print root
    print root.tag  # main tag
    # print root.attrib  # main attribute
    # for child in root:
    #    print child.tag, child.attrib

    # for neighbor in root.iter('sample'):
    #     print 'bla'
    #     print neighbor.attrib
    #
    # print root[0][8:]

    for country in root.findall('pwx/workout'):
        print 'bla'

    element = root.find('pwx/workout/sample')
    print element


def main():
    '''docstring'''
    # Not sure if this is really needed. TODO: check it

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts run files formats')

    parser.add_argument('-f',
                        '--file',
                        required=True,
                        help='run file that will be converted')

    parser.add_argument('-t',
                        '--type',
                        default='json',
                        help='output type of run file')

    args = vars(parser.parse_args())

    pwx_reader(args['file'])
