class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result=[]
        while(columnNumber>0):
            columnNumber-=1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber=columnNumber//26
        result.reverse()
        return ''.join(result)
        