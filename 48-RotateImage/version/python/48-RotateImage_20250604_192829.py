# Last updated: 04/06/2025, 19:28:29
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        # transpose+reverse
    def transpose(self,matrix):
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    def reflect(self,matrix):
        for row in matrix:
            row.reverse()
