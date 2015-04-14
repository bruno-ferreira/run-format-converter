
import argparse

parser = argparse.ArgumentParser(description='Converts  ')

parser.add_argument('--file', help='run file that will be converted')
parser.add_argument('--format', help='output format of run file')

args = parser.parse_args()

print args
