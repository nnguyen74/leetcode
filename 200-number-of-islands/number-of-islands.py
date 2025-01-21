from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = set()
        island = 0
        def visit(r, c):
            if r < 0 or r >= row_len or c < 0 or c >= col_len or (r, c) in visited or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            coords = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for coord in coords:
                new_r = r + coord[0]
                new_c = c + coord[1]
                if new_r >= 0 and new_r < row_len and new_c >= 0 and new_c < col_len and grid[new_r][new_c] == "1":
                    visit(new_r, new_c)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    visit(r, c)
                    island += 1
        
        return island

            