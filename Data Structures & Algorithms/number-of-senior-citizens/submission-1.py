class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age1, age2 = 0, 0
        count = 0

        for s in details:
            age1 = int(s[-4])
            if age1 < 6:
                continue
            age2 = int(s[-3])
            if (age1 * 10) + age2 > 60:
                count += 1 
        return count 
                