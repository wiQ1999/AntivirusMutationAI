from engine.blocks.block import Block
import numpy as np

class Single(Block):
    def __init__(self) -> None:
        super().__init__()
        self._area = np.array([[self.id]])

    @property
    def id(self) -> int:
        return 1
    
    @property
    def is_movable(self) -> bool:
        return False
    
    @property
    def is_winning(self) -> bool:
        return False
    
    @property
    def area(self) -> np.array:
        return self._area
