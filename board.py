from dataclasses import dataclass
from enum import Enum, auto
from typing import List


@dataclass
class Field:
    hit: bool = False
    has_ship: bool = False
    can_have_ship: bool = True

    def get_with_fog(self):
        if self.hit:
            return '*' if self.has_ship else 'X'
        else:
            return 'O'

    def get_private(self):
        if self.hit:
            return '*' if self.has_ship else 'X'
        elif self.has_ship:
            return 'S'
        else:
            return 'O'


class Board:
    def __init__(self, size: int):
        self.size = size
        self.fields: List[List[Field]] = [
            [Field() for _ in range(size)]
            for _ in range(size)
        ]

    def shoot(self, x: int, y: int) -> bool:
        field = self.fields[x][y]
        field.hit = True
        return field.has_ship

    def print_with_fog(self):
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
                print(f'{str(j)}  | {" ".join((x.get_with_fog() for x in row))}')
            else:
                print(f'{str(j)} | {" ".join((x.get_with_fog() for x in row))}')
            j += 1

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
                print(f'{str(j)}  | {" ".join((x.get_private() for x in row))}')
            else:
                print(f'{str(j)} | {" ".join((x.get_private() for x in row))}')
            j += 1
