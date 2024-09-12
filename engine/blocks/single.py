from engine.blocks.abc_block import AbcBlock
import numpy as np

class Single(AbcBlock):
    def __init__(self) -> None:
        super().__init__()
        self._area = np.array([[self.id]])

    @property
    def id(self) -> int:
        return 2
    
    @property
    def is_movable(self) -> bool:
        return False
    
    @property
    def is_winning(self) -> bool:
        return False
    
    @property
    def area(self) -> np.array:
        return self._area
