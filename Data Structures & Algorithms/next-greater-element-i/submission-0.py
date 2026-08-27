class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num_index = {num: i for i, num in enumerate(nums1)}
        #this give you the number and index in nums1: (4,0) [number 4 at index 0, etc]
        
        ans = [-1] * len(nums1)

        my_stack = []

        for num in nums2:
            cur = num
            while my_stack and cur > my_stack[-1]:
                val = my_stack.pop()
                index = num_index[val]
                ans[index] = num
            
            if cur in num_index: #this line is important. You need to make sure there is a place in the dict for the value of you will get an error
                my_stack.append(num)

        return ans


        

