class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output=0
        stack=[]
        for c in tokens:
            if c in '+-*/':
                b=int(stack.pop())
                a=int(stack.pop())
                if c=='+':
                    output=a+b
                elif c=='-':
                    output=a-b
                elif c=='*':
                    output=a*b
                elif c=='/':
                    output=a/b                    
                stack.append(output)
            else:
                stack.append(c)             
        return int(stack.pop())