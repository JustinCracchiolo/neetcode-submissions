class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        builtSubstring = ""
        p1, p2 = 0, 0

        while p1 < len(t) and p2 < len(s):
            if t[p1] == s[p2]:
                 builtSubstring += t[p1]
                 p1 += 1 
                 p2 += 1
            else:
                p2 += 1
        
        return len(t) - len(builtSubstring)

