class Solution:
    def climbStairs(self, n: int) -> int:
        
        #work backwards from n - 1 to 0
        #the total for the ith step is dp[i+1] + dp[i+2]
        #dp[n+1] = dp[n] = 1
        steps = [1] * (n+1)

        i = n - 2
        while(i >= 0):
            steps[i] = steps[i+1] + steps[i+2]
            i -= 1
        
        return steps[0]

