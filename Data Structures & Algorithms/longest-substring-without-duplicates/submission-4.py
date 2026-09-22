class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring=1
        n=len(s)
        if not s:
            return 0
        if n==1:
            return longest_substring

        substring=s[0]
        l,r=0,1
        while r<n:
            # print(substring)
            if s[r] not in substring:
                substring=substring + s[r]
                longest_substring=max(longest_substring,len(substring))
                r+=1
            else:
                l+=1
                substring=s[l:r]
            

        return longest_substring
                
