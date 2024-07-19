class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        points = sum(cardPoints[:k])
        max_points = points
        for i in range(1, k + 1):
            points += cardPoints[-i] - cardPoints[k - i]
            max_points = max(max_points, points)
        
        return max_points
            
        