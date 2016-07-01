class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """if n<2:
            return 1
        else:   
            return self.climbStairs(n-1)+self.climbStairs(n-2)"""
            
        s=[0 for i in range(n+1)]

        if n>2:
            s[1]=1
            s[2]=2
            for a in range(3,n+1):
                s[a]=s[a-1]+s[a-2]
        else:
            return n
        
        return s[a]