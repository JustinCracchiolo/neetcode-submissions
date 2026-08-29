class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        ans = [0] * n

        prefix_count = [0] * (n+1) #number of balls from 0 to i - 1 
        index_sum = [0] * (n + 1)  #sum of indices of balls from 0 to i - 1 

        for i in range(n):
            #if ball in bucket, add it to prev count
            prefix_count[i + 1] = prefix_count[i] + (boxes[i] == '1')

            #if ball in bucket, add 1 to the index sum
            index_sum[i + 1] = index_sum[i] + (i if boxes[i] == '1' else 0)

        for i in range(n):

            #get index sum and prefix sum for left of current pos
            left = prefix_count[i]
            left_sum = index_sum[i]

            #get index sum and prefix sum for right of current pos
            right = prefix_count[n] - prefix_count[i + 1]
            right_sum = index_sum[n] - index_sum[i + 1]

            ans[i] = (i * left - left_sum) + (right_sum - i * right)

        return ans