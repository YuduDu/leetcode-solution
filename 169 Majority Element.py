class Solution(object):
            
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        l = len(nums)
        return nums[l/2]