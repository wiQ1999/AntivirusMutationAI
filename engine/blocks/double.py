from engine.blocks.block import Block 
from engine.direction import Direction
import numpy as np

class Double(Block):
    def __init__(self, direction: Direction = Direction.North) -> None:
        self._area = np.array([[self.id, self.id]])
        self._rotate(direction)

    @property
    def id(self) -> int:
        return 2
    
    @property
    def is_movable(self) -> bool:
        return True
    
    @property
    def is_winning(self) -> bool:
        return True
    
    @property
    def area(self) -> np.array:
        return self._area
