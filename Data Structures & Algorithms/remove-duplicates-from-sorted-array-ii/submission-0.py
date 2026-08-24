class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        k = 0 #this pointer keeps track of first k elements in nums 

        left, right = 0, 0

        while left < n:
            count = 0
            
            while right < n and nums[left] == nums[right]:
                count += 1 
                right += 1 
            
            if count == 1:
                nums[k] = nums[left]
                k += 1
            else:
                nums[k], nums[k+1] = nums[left], nums[left]
                k += 2 
            left = right
        
        return k

