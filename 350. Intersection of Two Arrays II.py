class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r = []
        if len(nums1)*len(nums2)==0:
            return r
        else:
            if len(nums1)>len(nums2):
                tmp = nums1
                nums1 = nums2
                nums2 = tmp
                
            while nums1:
                i = nums1.pop()
                if i in nums2:
                    r.append(i)
                    nums2.remove(i)

                if len(nums2)==0:
                    break
            return r
                    
                