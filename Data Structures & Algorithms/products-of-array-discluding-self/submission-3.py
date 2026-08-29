class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = [1] #extra padding on left side 
        suffix_product = [1] #extra padding on right side

        for n in nums:
            prefix_product.append(n * prefix_product[-1])
        
        # O(1) appends during traversal
        for i in range(len(nums) - 1, -1, -1):
            suffix_product.append(nums[i] * suffix_product[-1])

        # Reverse suffix_product to align indices: O(N)
        suffix_product.reverse()
        ans = [1] * len(nums)

        for i in range(len(ans)):
            ans[i] = prefix_product[i] * suffix_product[i+1]
        
        return ans