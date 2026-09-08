class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        low,high=0,len(nums)-1


        while low<=high:
            mid=(high+low+1)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1

        return -1