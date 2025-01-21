from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        num_row = len(mat)
        num_col = len(mat[0])
        result = [[0 for j in range(num_col)] for i in range(num_row)]
        
        def getNeighbors(r, c):
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            neighbors = []
            for direction in directions:
                new_row = r + direction[0]
                new_col = c + direction[1]
                if new_row >= 0 and new_row < num_row and new_col >= 0 and new_col < num_col:
                    neighbors.append((new_row, new_col))
            return neighbors

        visited = set()
        check_queue = deque()
        for r in range(num_row):
            for c in range(num_col):
                if mat[r][c] == 0:
                    visited.add((r, c))
                    check_queue.append((r, c))
        current_layer = 1
        while check_queue:
            r, c = check_queue.popleft()
            neighbors = getNeighbors(r, c)
            for neighbor in neighbors:
                if neighbor not in visited:
                    result[neighbor[0]][neighbor[1]] = result[r][c] + 1
                    visited.add(neighbor)
                    check_queue.append(neighbor)
        return result
            

