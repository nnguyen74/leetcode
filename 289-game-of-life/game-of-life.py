class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        live_neighbor_board = [[0 for i in range(cols)] for j in range(rows)]
        def get_neighbors(r, c):
            directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            result = []
            for direction in directions:
                new_r = r + direction[0]
                new_c = c + direction[1]
                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols:
                    result.append([new_r, new_c])
            return result
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    for neighbor in get_neighbors(i, j):
                        live_neighbor_board[neighbor[0]][neighbor[1]] += 1
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    if live_neighbor_board[i][j] == 3:
                        board[i][j] = 1
                else:
                    if live_neighbor_board[i][j] < 2 or live_neighbor_board[i][j] > 3:
                        board[i][j] = 0
        