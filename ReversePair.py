class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[0]
        def merge_sort(nums):
            if(len(nums)<=1):
                return nums
            else:
                mid = len(nums)//2
                left = nums[:mid]
                right =nums[mid:]
                left = merge_sort(left)
                right = merge_sort(right)
                return merger(left,right)
        def merger(left,right):
            countIter(left,right)
            new = []
            i,j = 0,0
            while(i<len(left) and j<len(right)):
                if (left[i]<right[j]):
                    new.append(left[i])
                    i+=1
                else:
                    new.append(right[j])
                    j+=1
            new.extend(left[i:])
            new.extend(right[j:])
            return new
        def countIter(left,right):
            a = 0
            b = 0
            while(a<len(left) and b<len(right)):
                if left[a]>(2*right[b]):
                    temp=(len(left)-a)
                    result[0]+=temp
                    b+=1
                else:
                    a+=1
        sortedarr = merge_sort(nums)
        return result[0]
