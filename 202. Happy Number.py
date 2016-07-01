class Solution(object):
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def Happy(n):
            l = [int(i) for i in str(n)]
            print l
            if l not in self.L:
                self.L.append(l)
            else:
                return False
            new_n = sum([i**2 for i in l])
            if new_n==1:
                return True
            else:
                return Happy(new_n)
                
        self.L = []
        return Happy(n)