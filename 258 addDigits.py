class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num>=10:
            tmp = num
            t = 0
            while tmp>0:
                t = t+tmp%10
                tmp=tmp/10
            num = t
        
        return num