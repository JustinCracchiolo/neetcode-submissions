class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        letter_count = {}

        for char in text:
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1 
        
        if "l" in letter_count:
            letter_count["l"] //= 2 #since l is used twice we divide the count by 2

        if "o" in letter_count:
            letter_count["o"] //= 2 
            
        ballon = "balloon"
        max_count = len(text)
        
        for c in ballon:
            if c not in letter_count:
                return 0
            if c in letter_count:
                max_count = min(max_count, letter_count[c])
        
        return max_count

