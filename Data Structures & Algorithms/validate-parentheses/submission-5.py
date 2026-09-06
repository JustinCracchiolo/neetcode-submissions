class Solution:
    def isValid(self, s: str) -> bool:
        
        paren_stack = []

        for c in s:
            if c == '(' or c == "{" or c == "[":
                paren_stack.append(c)
            else:
                if len(paren_stack) > 0 and ((paren_stack[-1] == "(" and c == ")") or (paren_stack[-1] == "{" and c == "}") or (paren_stack[-1] == "[" and c == "]")):
                    paren_stack.pop()
                else:
                    return False 
        
        return len(paren_stack) == 0