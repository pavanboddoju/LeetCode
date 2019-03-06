class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)

        if m == 0:
            return matrix

        n = len(matrix[0])
        
        if n == 0:
            return []
        
        output = []        
        row, column = 0,0

        for i in range(m*n):
            output.append(matrix[row][column])
            
            if (row+column)%2 == 0:
                if column == n-1:
                    row += 1
                elif row == 0:
                    column += 1
                else:
                    row -= 1
                    column += 1
            else:
                if row == m-1:
                    column += 1
                elif column == 0:
                    row += 1
                else:
                    row += 1
                    column -= 1

        return output