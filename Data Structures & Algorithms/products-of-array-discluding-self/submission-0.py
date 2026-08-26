class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        output=[]
        zeros=0
        n=len(nums)
        for num in nums:
            if num != 0:
                mul=mul*num
            else:
                zeros+=1
        if zeros>1:
            return [0]*n

        output=[0]*n

        for i,num in enumerate(nums):
            if zeros == 1:
                output[i]=0 if num != 0 else mul
            else:
                output[i]=mul//num
        return output
