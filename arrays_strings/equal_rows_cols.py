"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


"""

from collections import defaultdict

def find_equal_rows_cols(grid):

    seen = defaultdict(int)

    n = len(grid)

    for i in range(n):
        seen[tuple(grid[i])] += 1
        print(f"row seen {i}: ", seen)
        col = []
        for j in range(n):
            col.append(grid[j][i])
        
        tuple_col = tuple(col)
        print("tuple_col : ", tuple_col)

        if tuple_col in seen:
            print("YESSSSSS: tuple col seen")
        seen[tuple(col)] += 1
        print(f"col seen: ", seen)

    print("seen: ", seen)

    ans = 0
    for key, value in seen.items():
        if value > 1:
            ans += 1
    
    return ans



def equalPairs(grid: list[list[int]]) -> int:
        def convert_to_key(arr):
            # Python is quite a nice language for coding interviews!
            return tuple(arr)
        
        dic = defaultdict(int)
        for row in grid:
            dic[convert_to_key(row)] += 1
        
        dic2 = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            
            dic2[convert_to_key(current_col)] += 1

        ans = 0
        for arr in dic:
            ans += dic[arr] * dic2[arr]
        
        return ans


if __name__ == "__main__":
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    # print(find_equal_rows_cols(grid))
    print(equalPairs(grid))

    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    # print(find_equal_rows_cols(grid))
    print(equalPairs(grid))
