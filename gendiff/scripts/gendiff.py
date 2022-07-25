#!/usr/bin/env python
import argparse
from gendiff import generate_diff

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
first_file = parser.add_argument('first_file')
second_file = parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    diff = generate_diff(args.first_file, args.second_file)
    return diff


if __name__ == '__main__':
    main()
