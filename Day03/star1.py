from collections import Counter
from typing import Union, Tuple
import re

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash(repr(self))

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Rectangle:

    def __init__(self, start: Point, size: Point):
        self.start = start
        self.size = size
        self.end = start + size

    def area(self) -> int:
        return self.size.x * self.size.y

    def overlapping(self, other: "Rectangle") -> int:
        dx = min(self.start.x, other.start.x) - max(self.end.x, other.end.x)
        dy = min(self.start.y, other.start.y) - max(self.end.y, other.end.y)

        if (dx >= 0) and (dy >= 0):
            return dx * dy

    def __iter__(self) -> "Rectangle":
        self.__iter_helper = self.start
        self.__helper_point = Point(1, 0)
        return self

    def __next__(self) -> Union[Point, StopIteration]:
        if self.__iter_helper == self.start:
            self.__iter_helper += self.__helper_point
            return self.start

        if self.__iter_helper.x >= self.end.x:
            self.__iter_helper = Point(self.start.x, self.__iter_helper.y + 1)

        if self.__iter_helper.y >= self.end.y:
            #print("Iteration should end.")
            raise StopIteration

        self.__iter_helper += self.__helper_point
        return self.__iter_helper


class Claim:

    def __init__(self, claim_id: int, zone: Rectangle):
        self.claim_id = claim_id
        self.zone = zone

    def __str__(self) -> str:
        return self.claim_id


matcher = re.compile("#(?P<claim_id>\d+) @ (?P<start>\d+,\d+): (?P<size>\d+x\d+)")

claims = {}

with open("./test_data.txt") as file:
    for line in file:
        result = matcher.match(line)

        start_x, start_y = result.group("start").split(",")
        start = Point(int(start_x), int(start_y))

        size_x, size_y = result.group("size").split("x")
        size = Point(int(size_x), int(size_y))

        rect = Rectangle(start, size)

        claim = Claim(int(result.group("claim_id")), rect)

        claims[result.group('claim_id')] = claim

fabric = []

for claim in claims.values():
    #print(f"Claim: {claim.claim_id}")

    for point in claim.zone:
        #print(f"Point: {point}")
        fabric.append(point)

fabric_counter = Counter(fabric)

overlapping = list(filter(lambda x: 1 < x[1], fabric_counter.items()))

print(overlapping)
print(len(overlapping))
