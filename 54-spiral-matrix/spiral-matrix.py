class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        directionIndex = 0
        visited = set()
        lenRow = len(matrix)
        lenCol = len(matrix[0])
        r = 0
        c = 0
        while len(res) != lenRow * lenCol:
            res.append(matrix[r][c])
            visited.add((r,c))
            newRow = directions[directionIndex][0] + r
            newCol = directions[directionIndex][1] + c
            if newRow < 0 or newRow >= lenRow or newCol < 0 or newCol >= lenCol or (newRow, newCol) in visited:
                directionIndex = directionIndex + 1 if directionIndex != 3 else 0
                r += directions[directionIndex][0]
                c += directions[directionIndex][1]
            else:
                r = newRow
                c = newCol
        return res
