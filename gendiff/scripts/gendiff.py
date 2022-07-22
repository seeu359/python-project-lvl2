import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    a = parser.add_argument('first_file')
    b = parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
