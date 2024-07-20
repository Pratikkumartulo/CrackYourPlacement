class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        lst=[]
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                stack=set()
                for k in range(j+1,len(nums)):
                    temp=target-(nums[i]+nums[j]+nums[k])
                    if temp in stack:
                        newlst=[nums[i],nums[j],nums[k],temp]
                        if newlst not in lst:
                            lst.append(newlst)
                    stack.add(nums[k])
        return lst