class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1 
        
        ans = []
        while k > 0:
            count = 0
            m = 0
            for f in freq:
                if freq[f] >= count:
                    count = freq[f]
                    m = f 
            ans.append(m)
            del freq[m]
            k -= 1 

        return ans 

