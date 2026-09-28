from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_len=float('inf')
        best_start=0
        need=Counter(t)
        missing=len(t)
        l=0
        

        if not s or not t or len(s)<len(t):
            return ""
        

        for r,ch in enumerate(s):
            # print("s[r]:",s[r])
            if need[ch]>0:
                missing-=1
            need[ch]-=1

            # print("cnt:",cnt)
            while missing==0:
                # print("while cnt loop entered")
                if r-l+1<best_len:
                    best_start,best_len=l,r-l+1
                    # print("l,r:",l,r)
                # print("l",l)
                
                need[s[l]]+=1
                if need[s[l]]>0:
                    missing+=1
                l+=1
            
                
        return "" if best_len==float('inf') else s[best_start:best_len+best_start]

