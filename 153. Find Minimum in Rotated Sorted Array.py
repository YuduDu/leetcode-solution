class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        begin = 0
        end = len(nums)
        
        m = nums[0]
        
        while begin < end:
            p = (begin+end)/2
            if nums[p]>nums[begin]:
                m = min(m,nums[begin])
                begin = p+1
            else:
                m = min(m,nums[p])
                end = p
        
        return m