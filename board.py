from dataclasses import dataclass
from enum import Enum, auto
from typing import List


@dataclass
class Field:
    hit: bool = False
    has_ship: bool = False
    can_have_ship: bool = True

    def __str__(self):
        if self.hit:
            return '*' if self.has_ship else 'X'
        else:
            return 'O'


class Board:
    def __init__(self, size: int):
        self.size = size
        self.fields: List[List[Field]] = [
            [Field()] * size for x in range(size)]

    def print(self):
        a = '     '
        for i in range(self.size):
            a += f'{chr(i+65)} '
        print(a)
        s = '   +'
        for i in range(self.size):
            s += '--'
        print(s)
        j = 1
        for row in self.fields:
            if j < 10:
                print(f'{str(j)}  | {" ".join((str(x) for x in row))}')
            else:
                print(f'{str(j)} | {" ".join((str(x) for x in row))}')
            j += 1
