class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        first = 0
        end = len(nums)
        
        while (first < end):
            p=(first+end)/2
            if nums[p]== target: return p
            elif nums[first] < nums[p]:
                if (target < nums[p]) and (target >= nums[first]):
                    end = p
                else: first = p+1
            else:
                if (target > nums[p]) and (target <= nums[end-1]):
                    first = p+1
                else:
                    end = p
        
        return -1