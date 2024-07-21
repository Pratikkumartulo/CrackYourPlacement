class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic={
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
        }
        res=""
        for i in sorted(dic.keys(), reverse=True):
            if num==0:
                break
            time = num//i
            while(time):
                res+=dic[i]
                time-=1
            num=num%i
        return res
        