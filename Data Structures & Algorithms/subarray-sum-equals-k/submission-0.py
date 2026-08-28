class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #keep track of current sum and differences at each index 
        # make a hashmap of difference => how many times 
        #for each current sum, check if the difference from k has been seen before. res += amount of times difference has been seen

        res, total = 0, 0

        diff_freq = { 0: 1 } #0 is always a difference

        for n in nums:
            total += n
            diff = total - k

            res += diff_freq.get(diff, 0)

            diff_freq[total] = 1 + diff_freq.get(total, 0)

        return res

