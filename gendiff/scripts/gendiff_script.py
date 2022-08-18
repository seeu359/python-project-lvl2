#!/usr/bin/env python
from gendiff.generate_diff import generate_diff
from gendiff.lib.parser import create_args


def main():
    args = create_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
