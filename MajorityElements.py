class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        max_count = 0
        majority_element = None
        for key, value in dic.items():
            if value > max_count:
                max_count = value
                majority_element = key
        
        return majority_element