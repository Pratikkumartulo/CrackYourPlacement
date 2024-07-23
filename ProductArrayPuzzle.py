class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        n = len(nums)
        middle=nums[n//2]
        count=0
        for i in range(n):
            count+=(abs(nums[i]-middle))
        return count
        