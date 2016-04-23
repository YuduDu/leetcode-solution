class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s)!=len(t)):
            return False
        
        dict_1={}
        dict_2 = {}
        for c in s:
            if c not in dict_1.keys():
                dict_1[c]=1
            else:
                dict_1[c]+=1
        for c in t:
            if c not in dict_2.keys():
                dict_2[c]=1
            else:
                dict_2[c]+=1
        return cmp(dict_1,dict_2)==0
            