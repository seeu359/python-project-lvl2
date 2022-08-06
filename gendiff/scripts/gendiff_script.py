#!/usr/bin/env python
from gendiff.formatters.stylish import stylish
from gendiff.generate_diff import generate_diff
from gendiff.parser import parsers_data
from gendiff.formatters.plain import plain


def main():
    args = parsers_data()
    diff = (generate_diff(args.first_file, args.second_file))
    if args.format == 'plain':
        return plain(diff)
    else:
        return stylish(diff)


if __name__ == '__main__':
    main()
