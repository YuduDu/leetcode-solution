class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for c in s:
            num=26*num+(ord(c)%64)
            
        return num