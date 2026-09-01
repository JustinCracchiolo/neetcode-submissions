class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # O (n log n)

        n = len(nums) 
        ans = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
            
            curr = a
            l, r = i + 1, n - 1
           
            while l < r:
                if curr + nums[l] + nums[r] == 0:
                    ans.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif curr + nums[l] + nums[r] > 0:
                    r -= 1 
                else:
                    l += 1 
        
        return ans