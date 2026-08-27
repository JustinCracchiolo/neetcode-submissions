class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
    def sumRange(self, left: int, right: int) -> int:
        sumrange = 0
        while left <= right:
            sumrange += self.arr[left]
            left += 1 
        return sumrange



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)