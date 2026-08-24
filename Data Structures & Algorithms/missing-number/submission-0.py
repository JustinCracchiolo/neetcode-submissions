class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            num_index = i
            while num_index < n and nums[i] != i:
                if nums[num_index] == i:
                    nums[i], nums[num_index] = nums[num_index], nums[i]
                else:
                    num_index += 1 
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return i + 1 