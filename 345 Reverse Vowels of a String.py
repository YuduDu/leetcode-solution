class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = ['a','o','e','u','i']
        v_l=[]
        s = list(s)
        for i in s:
            if i.lower() in v:
                v_l.append(i)

        for i in range(len(s)):
            if s[i].lower() in v:
                s[i]=v_l.pop()

        return "".join(s)