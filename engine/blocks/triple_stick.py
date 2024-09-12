from engine.blocks.abc_block import AbcBlock
from engine.direction import Direction
import numpy as np

class TripleStick(AbcBlock):
    def __init__(self, direction: Direction = Direction.North) -> None:
        self._area = np.array([[self.id, self.empty, self.empty],
                               [self.empty, self.id, self.id]])
        self._rotate(direction)

    @property
    def id(self) -> int:
        return 6
    
    @property
    def is_movable(self) -> bool:
        return True
    
    @property
    def is_winning(self) -> bool:
        return False
    
    @property
    def area(self) -> np.array:
        return self._area
