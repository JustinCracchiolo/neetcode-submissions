class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        freq = {}

        for char in arr:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        for char in arr:
            if freq[char] == 1:
                k -= 1 
            if k == 0:
                return char
        
        return ""
                