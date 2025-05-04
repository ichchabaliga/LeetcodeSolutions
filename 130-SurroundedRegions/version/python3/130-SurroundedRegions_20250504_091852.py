# Last updated: 04/05/2025, 09:18:52
# convert unsurrounded regions to Y, convert non Y's to X, then convert Y to O
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #phase 1: do DFS on corner o's and convert them to Ts

        #phase 2: convert non Ts to X


        #phase 3: convert Ts to o s

        ROWS,COLS=len(board),len(board[0])
        def capture(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]!='O':
                return 
            board[r][c]='Y'
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)



        for i in range(ROWS):
            for j in range(COLS):
                if i in [0,ROWS-1] or j in [0,COLS-1]:
                    capture(i,j)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]!='Y':
                    board[i][j]='X'
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=='Y':
                    board[i][j]='O'

                
