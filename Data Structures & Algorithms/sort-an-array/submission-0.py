class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        #merge sort 
        n = len(nums)

        if len(nums) == 1:
            return nums
        
        mid = n // 2

        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:n])

        merged = []

        while left and right:
            if left[0] <= right[0]:
                merged.append(left[0])
                left.pop(0)
            else:
                merged.append(right[0])
                right.pop(0)
        
        while left:
            merged.append(left[0])
            left.pop(0)
        
        while right:
            merged.append(right[0])
            right.pop(0)
        
        return merged

