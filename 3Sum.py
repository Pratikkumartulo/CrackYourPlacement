class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums,target,i):
            j = len(nums)-1
            while(i<j):
                if(nums[i]+nums[j]>target):
                    j-=1
                elif(nums[i]+nums[j]<target):
                    i+=1
                else:
                    while(i<j and nums[i]==nums[i+1]):
                        i+=1
                    while(i<j and nums[j]==nums[j-1]):
                        j-=1
                    result.append([-target,nums[i],nums[j]])
                    i+=1
                    j-=1
        result=[]
        if len(nums)<3:
            return []
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            n1=nums[i]
            target=-n1
            twoSum(nums,target,i+1)
        return result