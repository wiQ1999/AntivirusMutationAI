from engine.blocks.abc_triple_wave import AbcTriple
from engine.direction import Direction

class TripleWave2(AbcTriple):
    def __init__(self, direction: Direction = Direction.North) -> None:
        super().__init__(direction)

    @property
    def id(self) -> int:
        return 8
