from engine.blocks.block import Block 

class Double(Block):
    def __init__(self) -> None:
        super().__init__()
        self._area = [[self.id, self.id]]

    @property
    def id(self):
        return 2
    
    @property
    def is_movable(self):
        return True
    
    @property
    def is_winning(self):
        return True
    
    @property
    def area(self):
        return self._area
