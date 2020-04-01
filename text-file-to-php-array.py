#!/usr/bin/python3
# author: J.F.P. (Richard) Scholtens
# datum: 27/03/2020
# A program that takes in a text file and puts every line as it were an item
# in an PHP array format. It gives an text file as output. This can be useful
# for it is an efficiënt way to convert lists with text to a PHP array standard.
# An example for this can be a list of languages.

import sys


def main(argv):
    if len(argv) == 2 and argv[1][-4:] == '.txt':
        lst = []
        php_array = 'array('
        new_file = "PHP_array_" + argv[1][:-4]
        with open(new_file, "w+") as output_file:
            with open(argv[1], "r") as file:
                for line in file:
                    line = line.strip()
                    lst.append(line)
                lst.sort()
                for i in lst:
                    php_array += '"' + i + '", '
                php_array += ')'
                output_file.write(php_array)
    else:
        print("Usage: ./lesk.py example.txt", file=sys.stderr)
        exit(-1)
if __name__ == '__main__':
    main(sys.argv)
