class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if "" in strs:
            return ""
        res=strs[0]
        dic={}
        for i in strs[0]:
            dic[i]=i
        for i in range(1,len(strs)):
            if strs[i][0]!=res[0]:
                return ""
            else:
                j=0
                temp=res
                res=""
                k=0
                while(k<len(temp) and j<len(strs[i])):
                    if strs[i][j] == temp[k]:
                        res+=temp[k]
                    else:
                        break
                    j+=1
                    k+=1
        return res
                    