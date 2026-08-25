class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #could sort the array but thats is n logn 
        #using a hashmap time is n

        my_dict = {}
        max_element = 0 
        count = 0

        for x in nums:
            if x in my_dict:
                my_dict[x] += 1
            else:
                my_dict[x] = 1
            
            if my_dict[x] > count:
                    count = my_dict[x]
                    max_element = x
        
        return max_element

