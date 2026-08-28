class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        longest=0
        n=len(nums_set)
       

        for num in nums_set: 
            if num-1 not in nums_set:
                count=1
                cur_num=num
                while cur_num+1 in nums_set:                  
                    count+=1
                    cur_num+=1

                longest=max(longest,count)

        return longest