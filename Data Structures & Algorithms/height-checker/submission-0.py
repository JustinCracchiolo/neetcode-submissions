class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        #count how many times a certain height appears
        count = [0] * 101
        for h in heights:
            count[h] += 1

        #build an exepected array by filling out heights
        expected = []
        for h in range(1, 101):
            c = count[h]
            for _ in range(c): #number of occurences for that height
                expected.append(h)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res