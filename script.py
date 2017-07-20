# -*- coding: utf-8 -*-

import sys
import os

class Boards:
    def __init__(self, fileName, debugMode=False):
        self.__debugMode = debugMode
        self.file = self.__checkFileName(fileName)

    def __debug(self, text):
        if self.__debugMode:
            print text

    def readFile():
        pass

    def __checkFileName(self, fileName):
        if len(fileName) < 1:
            usage()
        try:
            file = open(fileName, 'r')
        except IOError:
            self.__debug('can\'t open file: ' + str(fileName))
            sys.exit(0)
        return file

def usage():
    print "usage:\n\t python script.py <filename>\n"
    sys.exit(0)

def main(argv):
    if len(argv) != 2:
        usage()
    boards = Boards(argv[1], debugMode=True)

if __name__ == '__main__':
    os.system('clear')
    main(sys.argv)
