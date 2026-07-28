class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        closed = [')', '}', ']']
        stack = []

        for c in s:
            if len(stack) == 0 and c in closed:
                return False 

            if c == ')' and len(stack):
                if stack[-1] != '(':
                    return False

                stack.pop()
                continue

            if c == ']':
                if stack[-1] != '[':
                    return False
                
                stack.pop()
                continue

            if c == '}':
                if stack[-1] != '{':
                    return False

                stack.pop()
                continue

            stack.append(c)
        
        if len(stack) > 0:
            return False

        return True
                
