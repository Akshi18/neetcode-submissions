class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        n=len(matrix)
        m=len(matrix[0])
        print(n,m)
        i=0

        if matrix[n-1][m-1]<target:
            return False

        while i<n:
            if matrix[i][m-1]==target:
                return True
            elif matrix[i][m-1]>target:
                row,low,high=i,0,m-1
                break
            else:
                i+=1
            
             
        
        
        while low<=high:
            mid=low+(high-low)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                low=mid+1
            else:
                high=mid-1

        return False