class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result