class Solution:
    def check(self, nums: List[int]) -> bool:

        #there should be at most one point where array is decreasing 

        dec_count = 0

        for i in range(len(nums)):
            if i == len(nums) - 1:
                if nums[0] < nums[i]:
                    dec_count += 1 
            else:
                if nums[i] > nums[i+1]:
                    dec_count += 1 
        
        return dec_count <= 1 
    