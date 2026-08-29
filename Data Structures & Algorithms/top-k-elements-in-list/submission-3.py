class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} #how many times each num appears
        freq = [[] for i in range(len(nums) + 1)] #freq[i] = [] of nums that appear i times

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, f in count.items():
            freq[f].append(num)

        ans = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
            if len(ans) == k:
                return ans
