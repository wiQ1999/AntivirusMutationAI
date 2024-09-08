from abc import ABC, abstractmethod

class Block(ABC):
    empty = 0

    @property
    @abstractmethod
    def id(self):
        return 0
    
    @property
    @abstractmethod
    def is_movable(self):
        return False
    
    @property
    @abstractmethod
    def is_winning(self):
        return False
    
    @property
    @abstractmethod
    def area(self):
        return [[]]

    @property
    def width(self):
        return len(self.area[0])

    @property
    def height(self):
        return len(self.area)
    
    def get_info(self):
        return f'id={self.id};movable={self.is_movable};winning={self.is_winning};width={self.width};height={self.height}'
    