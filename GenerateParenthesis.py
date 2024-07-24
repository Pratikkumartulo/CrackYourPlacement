class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def isValid(curr):
            count=0
            for i in curr:
                if i=="(":
                    count+=1
                else:
                    count-=1
                if count<0:
                    return False
            return count==0
        def solve(curr,open_count,close_count,n):
            if len(curr) == 2 * n:
                if isValid(curr):
                    result.append(curr)
                return
            if open_count < n:
                solve(curr + "(", open_count + 1, close_count, n)
            if close_count < open_count:
                solve(curr + ")", open_count, close_count + 1, n)
        curr = ""
        solve(curr, 0, 0, n)
        return result