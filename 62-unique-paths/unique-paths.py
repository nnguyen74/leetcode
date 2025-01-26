class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1]
        return matrix[m - 1][n - 1]
