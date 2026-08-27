class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #can contain duplicates 

        my_set = set()
        ans = []

        for n in nums:
            if n not in my_set:
                my_set.add(n)
            
        for i in range(1,len(nums)+1):
            if i not in my_set:
                ans.append(i)
            
        return ans