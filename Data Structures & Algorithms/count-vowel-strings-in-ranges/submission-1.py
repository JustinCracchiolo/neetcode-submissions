class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {"a", "e", "i", "o", "u"} # O(1) space

        prefix_cnt = [0] * (len(words) + 1) #keep track of how many times vowel start and end has been seen previously 

        prev = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefix_cnt[i + 1] = prev
        
        ans = [0] * len(queries)

        for i, q in enumerate(queries):
            l, r = q
            ans[i] = prefix_cnt[r + 1] - prefix_cnt[l]

        return ans


        