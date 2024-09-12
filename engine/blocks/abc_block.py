from abc import ABC, abstractmethod
from engine.direction import Direction
import numpy as np

class AbcBlock(ABC):
    empty = 0

    @property
    @abstractmethod
    def id(self) -> int:
        pass
    
    @property
    @abstractmethod
    def is_movable(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_winning(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def area(self) -> np.array:
        pass

    def is_possition_taken(self, x: int, y: int):
        return self._area[y, x] != self.empty

    @property
    def width(self) -> int:
        return len(self._area[0])

    @property
    def height(self) -> int:
        return len(self._area)
    
    def _rotate(self, direction: Direction) -> None:
        if direction == Direction.East:
            k = 1
        elif direction == Direction.South:
            k = 2
        elif direction == Direction.West:
            k = 3
        else:
            return
        self._area = np.rot90(self._area, k)
    
    def get_info(self) -> str:
        return f'id={self.id};movable={self.is_movable};winning={self.is_winning};width={self.width};height={self.height}'
    
    def print(self) -> None:
        line = ''.join(['+' for _ in range(len(self._area[0]))])
        print(line)
        for y in range(len(self._area)):
            print(self._area[y])
        print(line)
    