from engine.blocks.block import Block 

class Single(Block):
    def __init__(self) -> None:
        super().__init__()
        self._area = [[self.id]]

    @property
    def id(self):
        return 1
    
    @property
    def is_movable(self):
        return False
    
    @property
    def is_winning(self):
        return False
    
    @property
    def area(self):
        return self._area
