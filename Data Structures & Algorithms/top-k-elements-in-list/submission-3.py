class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        
        # Sort the dictionary keys by their values (frequencies) in descending order
        sorted_elements = sorted(seen.keys(), key=lambda x: seen[x], reverse=True)
        
        # Return the first k elements
        res = sorted_elements[:k]

        return res