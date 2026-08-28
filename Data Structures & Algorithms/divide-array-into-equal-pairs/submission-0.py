class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        num_freq = {}

        for n in nums:
            if n not in num_freq:
                num_freq[n] = 1
            else:
                num_freq[n] += 1 

        for n in num_freq:
            if num_freq[n] % 2 != 0:
                return False 

        return True