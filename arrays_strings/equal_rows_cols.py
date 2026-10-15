"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


"""

from collections import Counter


def equal_pairs(grid: list[list[int]]) -> int:
    rows = Counter(map(tuple, grid))
    cols = Counter(zip(*grid))

    return sum(count * cols[row] for row, count in rows.items())


if __name__ == "__main__":
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print(equal_pairs(grid))

    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equal_pairs(grid))
