class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_sum = [0]
        suffix_sum = [0]

        left, right = 1, len(nums) - 2 

        while left <= len(nums):
            prefix_sum.append(nums[left-1] + prefix_sum[left-1])
            suffix_sum.insert(0, nums[right+1] + suffix_sum[0])
            left += 1
            right -= 1 

        print(prefix_sum)
        print(suffix_sum)
        for i in range(len(prefix_sum)-1):
            if prefix_sum[i] == suffix_sum[i+1]:
                return i
        
        return -1


           