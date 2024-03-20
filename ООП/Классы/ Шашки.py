class Cell:
    def __init__(self, position) -> None:
        self.position = position

    def status(self):
        return self.position


class Checkers:
    def __init__(self) -> None:
        self.positions = {}
        self._create_positions()

    def _create_positions(self):
        for i in range(1, 9):
            for j in range(ord("A"), ord("H") + 1):
                if i <= 3 and (i + j) % 2 == 0:
                    self.positions[f"{chr(j)}{i}"] = Cell("W")
                elif i > 5 and (i + j) % 2 == 0:
                    self.positions[f"{chr(j)}{i}"] = Cell("B")
                else:
                    self.positions[f"{chr(j)}{i}"] = Cell("X")

    def move(self, f: str, t: str):
        self.positions[t] = self.positions[f]
        self.positions[f] = Cell("X")

    def get_cell(self, position):
        return self.positions[position]


checkers = Checkers()
for row in "87654321":
    for col in "ABCDEFGH":
        print(checkers.get_cell(col + row).status(), end="")
    print()
