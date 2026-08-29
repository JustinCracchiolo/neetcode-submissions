class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        freq = {} # O(1) because at most 26 keys

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1 
        
        new_s = ""
        
        #build letters that appear in order first because they are already in order
        for char in order:
            if char in freq:
                new_s += char * freq[char]
                del freq[char]
        
        #build letters not in order
        for char in freq:
            new_s += char * freq[char]

        return new_s

