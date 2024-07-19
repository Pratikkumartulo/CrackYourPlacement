class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_lst=[]
        col_lst=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row_lst.append(i)
                    col_lst.append(j)
        for i in row_lst:
            for k in range(len(matrix[0])):
                matrix[i][k]=0
        for j in col_lst:
            for k in range(len(matrix)):
                matrix[k][j]=0