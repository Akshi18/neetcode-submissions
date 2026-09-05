class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = []

        for i in range(n - 2):
            # skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result