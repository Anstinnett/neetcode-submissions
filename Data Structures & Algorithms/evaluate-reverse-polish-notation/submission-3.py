class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        
        for n in tokens:
            if n == "+" or n == "*" or n == "-" or n == "/":
                if n == "+":
                    x = int(stack.pop())
                    y = int(stack.pop())
                    z = x + y 
                    stack.append(z)
                elif n == "*":
                    x = int(stack.pop())
                    y = int(stack.pop())
                    z = x * y
                    stack.append(z)
                elif n =="-":
                    x = int(stack.pop())
                    y = int(stack.pop())
                    z = y - x
                    stack.append(z)
                elif n =="/":
                    x = int(stack.pop())
                    y = int(stack.pop())
                    z = int(y/x)
                    stack.append(z)   

            else:
                stack.append(int(n))

        return stack[0]

            