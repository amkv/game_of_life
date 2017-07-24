# -*- coding: utf-8 -*-

import sys
import os


class Board:
    def __init__(self, id_, delta, start_board, end_board):
        self.id = id_
        self.delta = delta
        self.start_board = start_board
        self.end_board = end_board
        self.start_board_str = None
        self.end_board_str = None

    def __str__(self):
        self.start_board_str = self._printed_board(self.start_board)
        self.end_board_str = self._printed_board(self.end_board)
        return "id: " + str(self.id) + \
                ", delta: " + str(self.delta) + "\n" + \
                "start:\n" + self.start_board_str + "\n" + \
                "end:\n" + self.end_board_str + "\n"

    def _printed_board(self, board):
        i = 0
        new_board = ""
        for each in board:
            if i == 20:
                new_board += '\n'
                i = 0
            if each == '0' or each == '0\n':
                new_board += ' .'
            else:
                new_board += ' #'
            i += 1
        return new_board

    def print_start(self):
        if self.start_board_str is None:
            self.start_board_str = self._printed_board(self.start_board)
        print self.start_board_str

    def print_end(self):
        if self.end_board_str is None:
            self.end_board_str = self._printed_board(self.end_board)
        print self.end_board_str

    def get_start(self): return self.start_board

    def get_end(self): return self.end_board

    def get_delta(self): return self.delta

    def get_id(self): return self.id


class Parser:
    def __init__(self, file_name, debug_mode=False):
        self._debug_mode = debug_mode
        self._my_file = self._check_file_name(file_name)

    # def __del__(self):
    #     self._my_file.close()

    def _debug(self, text):
        if self._debug_mode:
            print text

    def _check_file_name(self, file_name):
        if len(file_name) < 5:
            usage()
        if file_name[-4:] != '.csv':
            usage()
        try:
            my_file = open(file_name, 'r')
        except IOError:
            self._debug('can\'t open file: ' + str(file_name))
            sys.exit(0)
        try:
            next(my_file)       # skipping the first line with column names
        except StopIteration:
            usage()
        return my_file

    def _create_boards(self, line):
        info = line.split(',')
        try:
            return Board(info[0], info[1], info[2:402], info[402:802])
        except IndexError:
            usage()

    def _read_file(self):
        for line in self._my_file:
            yield line

    def next_board(self):
        try:
            line = self._read_file().next()
            return self._create_boards(line)
        except StopIteration:
            raise StopIteration


class Game:
    def __init__(self, board):
        self.board = board.get_start()
        self.delta = board.get_delta()
        pass


def usage():
    print "usage:\n\t python script.py <filename>\n"
    sys.exit(0)


def main(argv):
    if len(argv) != 2:
        usage()
    my_parser = Parser(argv[1], debug_mode=True)

    board = my_parser.next_board()
    board = my_parser.next_board()
    print board
    game = Game(board)


    # i = 0
    # while 42:
    #     try:
    #         # print my_parser.next_board()
    #         board = my_parser.next_board()
    #         del board
    #         i += 1
    #     except StopIteration:
    #         break
    # print i

if __name__ == '__main__':
    os.system('clear')
    main(sys.argv)
    sys.exit(0)
