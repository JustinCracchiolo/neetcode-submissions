class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        num_freq = {}
        max_num = -1

        for n in arr:
            if n not in num_freq:
                num_freq[n] = 1
            else:
                num_freq[n] += 1 

        for num in num_freq:
            freq = num_freq[num]

            if num == freq:
                max_num = max(max_num,num)

        return max_num