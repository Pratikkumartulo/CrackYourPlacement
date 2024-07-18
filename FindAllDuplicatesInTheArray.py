class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        dupes = set()
        for n in nums :  
            if n in seen :  
                dupes.add(n) 
            else:  
                seen.add(n) 
        return list(dupes)