class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #frequency counter for each letter (a=0, z=25)
            for char in s:
                count[ord(char) - ord('a')] += 1 
            res[tuple(count)].append(s) #make a tuple for each word of frequency of letters. Append that word to that frequency tuple 

        return list(res.values())