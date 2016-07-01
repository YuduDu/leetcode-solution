class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(0,len(nums)):
            t = 0-nums[i]
            
            if i == 0:
                new = nums[i+1:]
            elif i == len(nums)-1:
                new = nums[:i-1]
            else:
                new = nums[:i-1]+nums[i+1:]
            
            first = 0
            second = len(new)-1
            
            while first < second:
                if new[first]+new[second]==t:
                    tmp = [new[first],new[second],nums[i]]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
                    first+=1
                    second-=1
                elif new[first]+new[second]<t:
                    first+=1
                else:
                    second-=1
                    
        return result