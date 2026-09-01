class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #sliding window with two pointers right and left

        maxLength = 0
        seen = set()
        l = 0

        for r in range(len(s)):

            while s[r] in seen: #if duplicate then remove all elements in seen set
                seen.remove(s[l])
                l += 1 #stops when l = r
            
            seen.add(s[r]) #add current element to seen 
            maxLength = max(maxLength, r - l + 1)

        return maxLength


