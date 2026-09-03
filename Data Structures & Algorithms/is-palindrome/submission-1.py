import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r"\s+","",s)
        s=re.sub(r"[^a-zA-Z0-9]","",s).lower()
        n=len(s)
        print(n)
        output=True
        for i in range(int((n)//2)):
            print(f"s[i]:{s[i]},s[n-i]={s[n-i-1]}")
            if s[i]!=s[n-i-1]:
                output=False

        return output