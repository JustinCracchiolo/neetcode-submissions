class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        max_increase, max_decrease = 1, 1 
        increase_count, decrease_count = 1,1 

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                increase_count = 1
                decrease_count += 1 
            elif nums[i-1] < nums[i]:
                increase_count += 1
                decrease_count = 1
            else:
                increase_count = 1
                decrease_count = 1

            max_increase = max(increase_count, max_increase)
            max_decrease = max(decrease_count, max_decrease)

        return max(max_increase, max_decrease) 