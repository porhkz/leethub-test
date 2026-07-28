class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':0}
        stack = []

        for token in tokens:
            if token in operands:        
                right = int(stack.pop())
                left = int(stack.pop())
        
                if token == '/':
                    result = int(left / right)
                    stack.append(result)
                    continue

                result = int(operands[token](left, right))
                stack.append(result)
                continue 

            stack.append(token) 

        return stack.pop()