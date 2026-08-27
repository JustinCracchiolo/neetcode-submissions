class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        p = len(pattern)
        s = len(words)

        if p != s:
            return False 

        char_to_word = {}

        for i in range(len(words)):
            #check if letter is in dict, and if that letter it to the same word 
            if pattern[i] in char_to_word:
                if char_to_word[pattern[i]] != words[i]:
                    return False
            else: #check that given word is not in dict already 
                for w in char_to_word.values():
                    if w == words[i]:
                        return False 
                char_to_word[pattern[i]] = words[i]

        return True
