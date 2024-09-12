from typing import List, Tuple
from engine.blocks.abc_block import AbcBlock
from engine.direction import Direction
import numpy as np

class Board(object):
    _border = 2
    _finish = 1
    _empty = 0

    def __init__(self, direction: Direction, block_popsitions: List[Tuple[AbcBlock, int, int]]) -> None:
        self._direction = direction
        self._block_positions = block_popsitions
        self._init_board()
        self._draw_blocks()

    def _init_board(self) -> None:
        if self._direction == Direction.North:
            self._board = np.array(
                [[self._finish] + [self._border] * 5] + 
                [[self._empty] * 5 + [self._border] for _ in range(5)])
        elif self._direction == Direction.East:
            self._board = np.array(
                [[self._empty] * 5 + [self._finish]] +
                [[self._empty] * 5 + [self._border] for _ in range(4)] +
                [[self._border] * 6])
        elif self._direction == Direction.South:
            self._board = np.array(
                [[self._border] + [self._empty] * 5 for _ in range(5)] +
                [[self._border] * 5 + [self._finish]])
        elif self._direction == Direction.West:
            self._board = np.array(
                [[self._border] * 6] +
                [[self._border] + [self._empty] * 5 for _ in range(4)] +
                [[self._finish] + [self._empty] * 5])

    def _draw_blocks(self) -> None:
        for bp in self._block_positions:
            b, x, y = bp
            for b_y in range(len(b.area)):
                new_y = y + b_y
                for b_x in range(len(b.area[0])):
                    new_x = x + b_x
                    if self._is_position_free(new_x, new_y):
                        if b.is_possition_taken(b_x, b_y):
                            self._board[new_y][new_x] = b.id
                    else:
                        raise Exception(f'Posision (x:{new_x}, y:{new_y}) is taken.')
                
    def _is_position_free(self, x: int, y: int) -> bool:
        return self._board[y][x] == 0

    def print(self) -> None:
        line = ''.join(['-' for _ in range(len(self._board[0]))])
        print(line)
        for y in range(len(self._board)):
            print(self._board[y])
        print(line)
