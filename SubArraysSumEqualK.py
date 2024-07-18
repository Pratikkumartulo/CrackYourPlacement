class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        dic = {0:1}
        sums= 0
        for i in range (len(nums)):
            sums+=nums[i]
            if sums - k in dic:
                count += dic[sums - k]
            if sums in dic:
                dic[sums]+=1
            else:
                dic[sums]=1
        return count