class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        zeroP = []
        i=0

        #while i <l:
        #    if nums[i]==0:
        #        zeroP.append(i)
        #    else:
        #        if zeroP!=[]:
        #            p=zeroP.pop(0)
        #            nums[p] = nums[i]
        #            nums[i]=0
        #            i-=1
        #    i+=1
        l =len(nums)
        i=0
        n=0
        while n<l:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            n+=1
 
                
        