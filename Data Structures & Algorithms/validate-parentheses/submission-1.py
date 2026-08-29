class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cl_to_op={')':'(',']':'[','}':'{'}
        

        for b in s:
            if b in cl_to_op:
                if not stack or stack[-1]!=cl_to_op[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        return not stack 

                




        