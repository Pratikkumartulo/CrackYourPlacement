from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        num_set = set(arr)
        if x==0:
            seen=set()
            for i in arr:
                if i in seen:
                    return 1
                seen.add(i)
            return -1
        for i in arr:
            if (x+i) in num_set:
                return 1
        return -1