class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x=0
        l=len(nums)
        flag=False
        for i in range(1,l):
            x=nums[i-1]
            if nums[i]==x:
                flag = True

        return flag


            
