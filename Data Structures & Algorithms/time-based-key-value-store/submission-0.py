
class TimeMap:

    def __init__(self):
        self.store={}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        
        if timestamp not in self.store[key]:
            self.store[key].append([timestamp,value])

        

    def get(self, key: str, timestamp: int) -> str:

        res,values="",self.store.get(key,[])
        lo,high=0,len(values)-1

        while lo<=high:
            mid=lo+(high-lo)//2
            if values[mid][0]<=timestamp:
                res=values[mid][1]
                lo=mid + 1
            else:
                high=mid-1

        return res
