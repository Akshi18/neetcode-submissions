class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        

        while left<right:
            
            cur_num= numbers[left] + numbers[right]

            if cur_num==target:
                return [left+1,right+1]
            elif cur_num<target:
                left +=1
            else:
                right-=1

            
