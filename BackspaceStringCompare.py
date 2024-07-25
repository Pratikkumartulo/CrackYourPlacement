class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1=[]
        list2=[]
        i=0
        while(i<len(s)):
            if s[i]=="#":
                if list1:
                    list1.pop()
            else:
                list1.append(s[i])
            i+=1
        i=0
        while(i<len(t)):
            if t[i]=="#":
                if list2:
                    list2.pop()
            else:
                list2.append(t[i])
            i+=1
        return list1==list2
        