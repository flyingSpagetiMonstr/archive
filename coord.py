# import matrix


class Coord:
    def __init__(self, i: int, j: int, parent=None):
        self.i = i
        self.j = j
        # if parent:
        self.parent = parent
        pass

    def __str__(self) -> str:
        return f"({self.i},{self.j})"

    def __add__(self, vector):
        return Coord(self.i + vector.i, self.j + vector.j)

    def __sub__(self, vector):
        return Coord(self.i - vector.i, self.j - vector.j)

    def __eq__(self, __o: object) -> bool:
        if type(__o) != Coord:
            return False
        return self.i == __o.i and self.j == __o.j

    def __abs__(self) -> float:
        return (self.i**2+self.j**2)**(0.5)

    def copy(self):
        return Coord(self.i, self.j)

    # return adjacent nodes of self, in a cerntain graph
    def adjacencies(self, graph) -> list:
        lis: list[Coord] = []
        for i in range(4):
            adj = self+directions[i]
            adj.parent = self
            try:
                if graph[adj.i][adj.j] != 1:
                    lis.append(adj)
            except IndexError:
                pass
        return lis


class Direction(Coord):
    strs = ["Down", "Right", "Up", "Left"]
    original_coords = [Coord(1, 0), Coord(
        0, 1), Coord(-1, 0), Coord(0, -1)]  # anticlockwise

    class NotADirectionError(Exception):
        pass

    def __init__(self, i: int, j: int):
        super().__init__(i, j)
        try:
            self.index = Direction.original_coords.index(self)
        except ValueError:
            raise Direction.NotADirectionError("This coord is not a direction")

    def __str__(self) -> str:
        return Direction.strs[self.index]


directions = [Direction(1, 0), Direction(
    0, 1), Direction(-1, 0), Direction(0, -1)]  # anticlockwise

# directions = [Coord(1, 0), Coord(0, 1), Coord(-1, 0),
#               Coord(0, -1)]  # anticlockwise
