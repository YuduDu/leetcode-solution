class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        begin = 0
        end = len(nums)
        
        while begin<end:
            p = (begin+end)/2
            if nums[p]==target: return True
            elif nums[p]>nums[begin]:
                if (nums[begin]<=target) and (nums[p]>target):
                    end = p
                else:
                    begin = p+1
            elif nums[p]<nums[begin]:
                if (nums[p] < target) and (nums[end-1]>=target):
                    begin = p+1
                else:
                    end = p
            else:
                begin +=1
        return False