class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring=0
        n=len(s)
        l=0
        charset=set()

        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            longest_substring=max(longest_substring,r-l+1)

        return longest_substring

                
