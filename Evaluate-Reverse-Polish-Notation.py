class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        stack = []

        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                op = c
                op1 = stack.pop()
                op2 = stack.pop()
                op1 = int(op1)
                op2 = int(op2)

                if op == "+":
                    stack.append(str(op1+op2))
                elif op == "-":
                    stack.append(str(op2-op1))
                elif op == "*":
                    stack.append(str(op1*op2))
                elif op == "/":
                    stack.append(str(int((op2 / op1))))
        
        return int(stack[-1])
            
        
                
