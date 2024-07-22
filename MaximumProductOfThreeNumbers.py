class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        prod1 = nums[0] * nums[1] * nums[2]
        prod2 = nums[0] * nums[1] * nums[-1]
        prod3 = nums[0] * nums[-2] * nums[-1]
        prod4 = nums[-1] * nums[-2] * nums[-3]
        return max(prod1,prod2,prod3,prod4)