class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cl_to_op={')':'(',']':'[','}':'{'}

        for b in s:
            if b in cl_to_op:
                if stack and stack[-1]==cl_to_op[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False

                




        