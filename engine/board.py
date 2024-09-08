from typing import List, Tuple
from engine.blocks.block import Block
from engine.direction import Direction

class Board(object):
    _border = -1
    _empty = 0

    def __init__(self, direction: Direction, block_popsitions: List[Tuple[Block, Direction, int, int]]):
        #if (any(db for db in directed_blocks)):
        #    raise Exception('No winning block in blocks collection.')
        #self.blocks = directed_blocks
        self._direction = direction
        self._block_positions = block_popsitions
        self._init_board()

    def _init_board(self):
        if self._direction == Direction.North:
            self._board = [
                [self._empty] + [self._border for _ in range(4)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)]
            ]
        if self._direction == Direction.East:
            self._board = [
                [self._empty for _ in range(6)], 
                [self._empty for _ in range(5)] + [self._border], 
                [self._empty for _ in range(5)] + [self._border], 
                [self._empty for _ in range(5)] + [self._border], 
                [self._empty for _ in range(5)] + [self._border]
            ]
        if self._direction == Direction.South:
            self._board = [
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._empty for _ in range(5)], 
                [self._border for _ in range(4)] + [self._empty], 
            ]
        if self._direction == Direction.West:
            self._board = [
                [self._border] + [self._empty for _ in range(5)], 
                [self._border] + [self._empty for _ in range(5)], 
                [self._border] + [self._empty for _ in range(5)], 
                [self._border] + [self._empty for _ in range(5)], 
                [self._empty for _ in range(6)]
            ]

    def print(self):
        line = ''.join(['-' for _ in range(len(self._board[0]))])
        print(line)
        for y in range(len(self._board)):
            print(self._board[y])
        print(line)

