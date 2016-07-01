class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l=[]
        if s:
            for i in range(len(s)-1):
                if dictionary[s[i]]<dictionary[s[i+1]]:
                    l.append(-dictionary[s[i]])
                else:
                    l.append(dictionary[s[i]])
                    
            l.append(dictionary[s[-1]])
            print l
            return sum(l)
                
                
        else:
            return None
        
        