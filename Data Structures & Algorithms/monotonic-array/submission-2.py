class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isMonotoneDec = True
        isMonotoneInc = True

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] < nums[i+1]:
                isMonotoneDec = False 
            elif nums[i] > nums[i+1]:
                isMonotoneInc = False 
        
        return isMonotoneInc or isMonotoneDec
            