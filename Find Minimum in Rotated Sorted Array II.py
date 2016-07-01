class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums)
        
        m = nums[0]
        
        while begin<end:
            
            p=(begin+end)/2
            
            if nums[begin] < nums[p]:
                m = min(m, nums[begin])
                begin = p+1
            elif nums[begin]>nums[p]:
                m = min(m,nums[p])
                end = p
            else:
                m = min(m,nums[begin])
                begin+=1
        
        return m