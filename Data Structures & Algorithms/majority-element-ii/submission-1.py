class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        ans = []

        for f in freq:
            if freq[f] > n/3:
                ans.append(f)

        return ans