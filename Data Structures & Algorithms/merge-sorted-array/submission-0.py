class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #three pointers 
        #one is the traversal backwards through nums1
        #one is the traversal backwards of nums1 starting from m - 1 
        #one is traversal backwards of nums2 starting from n - 1 

        p1, p2, index = m - 1, n - 1, len(nums1) - 1 

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1 
            else:
                nums1[index] = nums2[p2]
                p2 -= 1 
            index -= 1 

        while p1 >= 0:
            nums1[index] = nums1[p1]
            p1 -= 1 
            index -= 1
        
        while p2 >= 0:
            nums1[index] = nums2[p2]
            p2 -= 1 
            index -= 1

        
