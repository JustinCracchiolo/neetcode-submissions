class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #Time: O(n)
        #Space: O(n)
        
        index = 0
        ans = []

        while len(ans) < 2 * len(nums):
            if index == len(nums):
                index = 0
            ans.append(nums[index])
            index += 1
        
        return ans