class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        letter_index_map = {char: i for i, char in enumerate(order)} # O(1) space 

        new_s = ""

        not_in_order = "" #for letters that are not in order. Just add them on at the end

        for i, char in enumerate(s):
            if char not in letter_index_map:
                not_in_order += char 
                continue
            index = 0
            #sliding window
            while index < len(new_s) and letter_index_map[new_s[index]] <= letter_index_map[char]:
                index += 1 
            new_s = new_s[:index] + char + new_s[index:]

        return new_s + not_in_order