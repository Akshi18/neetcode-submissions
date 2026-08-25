class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=''
        for st in strs:
            en_str=str(len(st))+'#'+st
            encoded_string=encoded_string+en_str

        return encoded_string


    def decode(self, s: str) -> List[str]:
        print(s)
        ls=[]
        n=len(s)
        i=0
        while i<n:
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            print(length)
            start=j+1
            ls.append(s[start:start+length])
            i=start+length
        return ls




