class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        finish = 0
        wait = 0
        n = len(customers)

        for q in customers:
            if finish >= q[0]:
                finish = finish - q[0] + (q[0] + q[1])
            else:
                finish = q[0] + q[1]
            
            wait += (finish - q[0])
        
        return wait / n