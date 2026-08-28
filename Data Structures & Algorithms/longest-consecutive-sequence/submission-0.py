class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0
        count = 1

        for num in nums:
            if num - 1 not in numSet: #beginning of sequence
                count = 1
                n = num
                while n + 1 in numSet:
                    count += 1 
                    n += 1 
                longest = max(count, longest)
        
        return longest
