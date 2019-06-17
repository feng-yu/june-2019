"""
[Medium]

You are given an array of non-negative integers that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
and 3 in the fourth index (we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""
from functools import reduce


def solution(data):
    total = 0
    while data:
        if len(data) == 1:
            return total
        #handle if the left_edge is higher than right_edge
        if data[0] > data[-1]:
            data.reverse()

        left_edge = data[0]
        for i, value in enumerate(data[1:]):
            if value >= left_edge:
                level = value if value < left_edge else left_edge
                if i > 0:
                    to = reduce(lambda a, b: a + b, list(map(lambda x: level-x, data[1:i+1])))
                    total += to
                data = data[i+1:]   #data[0] was used as left_edge
                break



data = [2,1,2]
data1 = [3, 0, 1, 3, 0, 5]
data2 = [3, 0, 1, 4, 0, 3]
data3 = [4, 2, 3]

print(solution(data))
print(solution(data1))
print(solution(data2))
print(solution(data3))