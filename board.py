from typing import List


class Board:
    def __init__(self, size):
        self.fields: List[List[str]] = [["O"] * size for x in range(size)]

    def print(self):
        a = '*  '
        for i in range(len(self.fields[0])):
            a += chr(i+65) + ' '
        print(a)
        s = '*+'
        for i in range(len(self.fields[0])):
            s += '--'
        print(s)
        j = 1
        for row in self.fields:
            if j < 10:
                print(str(j) + ' |' + " ".join(row))
            else:
                print(str(j) + '|' + " ".join(row))
            j += 1
