class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]

        nums=sorted(nums)
        print(nums)

        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum==0:
                    if [nums[i],nums[left],nums[right]] in result:
                        left+=1
                    else:
                        result.append([nums[i],nums[left],nums[right]])
                        left+=1
                elif cur_sum<0:
                    left+=1
                else:
                    right-=1

        return result

