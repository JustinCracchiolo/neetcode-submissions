class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        ans = [[1]]
        prev_row = [1]

        for i in range(1, numRows):
            current_row = [1] * (i + 1)
            for j in range(1, i):
                current_row[j] = prev_row[j-1] + prev_row[j]
            ans.append(current_row)
            prev_row = current_row 
        
        return ans

