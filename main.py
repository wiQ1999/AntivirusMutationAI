from engine.blocks.single import Single
from engine.blocks.double import Double
from engine.blocks.double_oblique import DoubleOblique
from engine.direction import Direction
from engine.board import Board

s1 = Single()
d1 = Double()
do1 = DoubleOblique()

print(f's1: {s1.get_info()}')
print(f'd1: {d1.get_info()}')
print(f'do1: {do1.get_info()}')

Board(Direction.North, []).print()
Board(Direction.East, []).print()
Board(Direction.South, []).print()
Board(Direction.West, []).print()
