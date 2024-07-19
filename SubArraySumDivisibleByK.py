class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums=0
        dic={0:1}
        res=0
        for i in range(len(nums)):
            sums+=nums[i]
            rem = sums%k
            if rem<0:
                rem+=k
            if rem in dic:
                res+=dic[rem]
                dic[rem]+=1
            else:
                dic[rem]=1
        return res
        