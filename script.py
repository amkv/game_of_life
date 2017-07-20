# -*- coding: utf-8 -*-

import sys
import os

class Parser:
    def __init__(self, fileName, debugMode=False):
        self._DebugMode = debugMode
        self.File = self._check_file_name(fileName)

    def _debug(self, text):
        if self._DebugMode:
            print text

    def _check_file_name(self, fileName):
        if len(fileName) < 1:
            usage()
        try:
            myFile = open(fileName, 'r')
        except IOError:
            self._debug('can\'t open file: ' + str(fileName))
            sys.exit(0)
        return myFile

    def read_file(self):
        pass

def usage():
    print "usage:\n\t python script.py <filename>\n"
    sys.exit(0)

def main(argv):
    if len(argv) != 2:
        usage()
    MyParser = Parser(argv[1], debugMode=True)
    MyParser.read_file()


if __name__ == '__main__':
    os.system('clear')
    main(sys.argv)
