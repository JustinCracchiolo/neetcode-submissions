class Solution:
    def maxDifference(self, s: str) -> int:
        
        freq_dict = {}
        max_odd, min_even = 1, len(s)
        #max difference will be biggest_odd - smallest_even

        for char in s:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1 
            
        for freq in freq_dict:
            if(freq_dict[freq] % 2 == 0):
                min_even = min(min_even, freq_dict[freq])
            else:
                max_odd = max(max_odd, freq_dict[freq])


        return max_odd - min_even