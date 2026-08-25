class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        difference = {} # difference => index
        n = len(nums)

        for i in range(n):
            if nums[i] not in difference:
                diff = target - nums[i]
                difference[diff] = i
            else:
                return [min(i, difference[nums[i]]), max(i, difference[nums[i]])]

