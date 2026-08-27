class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board[0])
        m=len(board)
        output=True
        for i in range(0,n):
            seen_A={}
            for j in range(0,m):
                if board[i][j]!='.':
                    if board[i][j] not in seen_A:
                        seen_A[board[i][j]]=1
                    
                    else:
                        print("seen_A")
                        print(seen_A)
                        output=False

        for j in range(0,m):
            seen_B={}
            for i in range(0,n):
                if board[i][j]!='.':
                    if board[i][j] not in seen_B:
                        seen_B[board[i][j]]=1
                    else:
                        print("seen_B")
                        print(seen_B)
                        output=False
        a=0
        b=0
        for i in range(0,n,3):
            for j in range(0,m,3):
                seen_S={}
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l]!='.':
                            if board[k][l] not in seen_S:
                                seen_S[board[k][l]]=1
                                print(f"k={k},l={l}")
                                print("seen_S")
                                print(seen_S)
                            else:
                                print("seen_S")
                                print(seen_S)
                                output=False

        return output


        