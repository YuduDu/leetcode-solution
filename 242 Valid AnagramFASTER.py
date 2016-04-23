class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
            if len(s)==0:
                return True
            dict = [0 for i in range(125)]
            for c in s:
                dict[ord(c)]+=1
            for c in t:
                dict[ord(c)]-=1
                if dict[ord(c)]<0:
                    return False
            return True