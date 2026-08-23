class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #make a dictionary. 
        #Traverse both strings. For each letter increment the count for each letter
        #the count should be even at the end

        #base case where the lengths aren't the same
        if len(s) != len(t):
            return False

        my_dict = {}
        index = 0

        while index < len(s):
            if s[index] not in my_dict:
                my_dict[s[index]] = 1
            else:
                my_dict[s[index]] += 1

            index += 1 
        
        index = 0
        while index < len(t):
            if t[index] not in my_dict:
                return False
            else:
                my_dict[t[index]] += 1
            
            index += 1
        
        for c in my_dict.values():
            if c % 2 != 0:
                return False 
        
        return True