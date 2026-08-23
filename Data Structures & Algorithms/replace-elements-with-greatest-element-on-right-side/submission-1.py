class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        current_max = -1
        n = len(arr) - 1 

        for i in range(n, -1, -1):
            temp = arr[i]
            if i == n:
                arr[i] = -1
            else:
                arr[i] = current_max
            
            current_max = max(current_max, temp)

        return arr