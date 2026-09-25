class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt={}
        s2_cnt={}
        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            s1_cnt[s1[i]]=s1_cnt.get(s1[i],0)+1
            s2_cnt[s2[i]]=s2_cnt.get(s2[i],0)+1

        l=0
        for r in range(len(s1),len(s2)):
            if s1_cnt==s2_cnt:
                return True
   
            s2_cnt[s2[r]]=s2_cnt.get(s2[r],0)+1
            s2_cnt[s2[l]]-=1
            if s2_cnt[s2[l]]==0:
                del s2_cnt[s2[l]]

            l+=1

        if s1_cnt==s2_cnt:
            return True
        return False