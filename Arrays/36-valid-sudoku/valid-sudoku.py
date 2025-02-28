class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[0]*9 for _ in range(9)]
        col=[[0]*9 for _ in range(9)]
        box=[[0]*9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue


                pos=int(board[r][c])-1
                if row[r][pos]==1:
                    return False
                row[r][pos]=1
                if col[c][pos]==1:
                    return False
                col[c][pos]=1

                boxidx=(r//3)*3 + c//3

                if box[boxidx][pos]==1:
                    return False

                box[boxidx][pos]=1
        return True
        