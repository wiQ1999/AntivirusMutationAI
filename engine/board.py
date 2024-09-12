from typing import List, Tuple
from engine.blocks.abc_block import AbcBlock
from engine.direction import Direction
import numpy as np

class Board(object):
    _border = 2
    _finish = 1
    _empty = 0

    def __init__(self, direction: Direction, block_popsitions: List[Tuple[AbcBlock, int, int]]) -> None:
        self.direction = direction
        self._block_positions = block_popsitions
        self._init_board()
        self._draw_blocks()

    @property
    def width(self) -> int:
        return len(self._area[0])
    
    @property
    def height(self) -> int:
        return len(self._area)

    def _init_board(self) -> None:
        if self.direction == Direction.North:
            self._area = np.array(
                [[self._finish] + [self._border] * 5] + 
                [[self._empty] * 5 + [self._border] for _ in range(5)])
        elif self.direction == Direction.East:
            self._area = np.array(
                [[self._empty] * 5 + [self._finish]] +
                [[self._empty] * 5 + [self._border] for _ in range(4)] +
                [[self._border] * 6])
        elif self.direction == Direction.South:
            self._area = np.array(
                [[self._border] + [self._empty] * 5 for _ in range(5)] +
                [[self._border] * 5 + [self._finish]])
        elif self.direction == Direction.West:
            self._area = np.array(
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
                    if b.is_position_taken(b_x, b_y):
                        if self._is_position_free(new_x, new_y):
                            self._area[new_y, new_x] = b.id
                        else:
                            raise Exception(f'Posision (x:{new_x}, y:{new_y}) is taken.')
                
    def _is_position_free(self, x: int, y: int) -> bool:
        pos = self._area[y, x]
        return pos == self._empty or pos == self._finish

    def print(self) -> None:
        line = ''.join(['-' for _ in range(len(self._area[0]))])
        print(line)
        for y in range(len(self._area)):
            print(self._area[y])
        print(line)
