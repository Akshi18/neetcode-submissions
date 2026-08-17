class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for s in strs:
            arr=[0] * 26
            for ch in s:
                index=ord(ch) - ord ('a')
                arr[index]+=1
            key=tuple(arr)

            if key not in groups:
                groups[key]=[]
            groups[key].append(s)

        return list(groups.values())




  
