class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{","]":"[" }
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                opening_tag = pairs[c]
                if stack == [] or not (stack[-1] == opening_tag):
                    return False
                else:
                    stack.pop()
        
        if stack == []:
            return True
        return False
            
        