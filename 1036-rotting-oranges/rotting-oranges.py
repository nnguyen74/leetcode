from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_row = len(grid)
        len_col = len(grid[0])
        # From a coord, get orange neighbors - 0(1)
        def get_fresh_orange_neighbors(coord):
            r, c = coord
            neighbors = []
            if r - 1 >= 0:
                neighbors.append((r - 1, c))
            if r + 1 < len_row:
                neighbors.append((r + 1, c))
            if c - 1 >= 0:
                neighbors.append((r, c - 1))
            if c + 1 < len_col:
                neighbors.append((r, c + 1))
            return [neighbor for neighbor in neighbors 
                if grid[neighbor[0]][neighbor[1]] == 1]
        minute = -1
        rotten_oranges = []
        # Get rotten oranges O(mn)
        for r in range(len_row):
            for c in range(len_col):
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
        # Check the spread
        orange_queue = deque(rotten_oranges)
        while True:
            minute += 1
            next_minute = deque()
            while orange_queue:
                rotten_orange = orange_queue.popleft()
                fresh_oranges = get_fresh_orange_neighbors(rotten_orange)
                print(rotten_orange, fresh_oranges, minute)
                for fresh_orange in fresh_oranges:
                    r, c = fresh_orange
                    grid[r][c] = 2
                next_minute.extend(fresh_oranges)
            print(minute, next_minute)
            orange_queue = next_minute
            if not orange_queue:
                break

        for r in range(len_row):
            for c in range(len_col):
                if grid[r][c] == 1:
                    return -1
        return minute


