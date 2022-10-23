#!/usr/bin/env python
from gendiff.generate_diff import generate_diff
from gendiff.cli import get_parser_args


def main():
    try:
        args = get_parser_args()
        print(generate_diff(args.first_file, args.second_file, args.format))
    except TypeError:
        print('One of the file types is not supported!')


if __name__ == '__main__':
    main()
