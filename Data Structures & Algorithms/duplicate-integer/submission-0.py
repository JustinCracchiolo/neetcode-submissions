class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Have a set with all previous seen numbers
        #Check if number is in set 

        #Time: O(n)
        #Space: O(n) 

        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        
        return False