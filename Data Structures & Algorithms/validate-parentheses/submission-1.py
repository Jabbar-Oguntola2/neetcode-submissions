class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                opening_tag = ""
                if c == ")":
                    opening_tag = "("
                elif c == "]":
                    opening_tag = "["
                else:
                    opening_tag = "{"
                if stack == [] or not (stack[-1] == opening_tag):
                    return False
                else:
                    stack.pop()
        
        if stack == []:
            return True
        return False
            
        