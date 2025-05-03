# Last updated: 03/05/2025, 18:40:12
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows,cols=len(rooms),len(rooms[0])
        q=deque()
        visited=set()

        def addRoom(row,col):
            if (row<0 or col <0 or row>=rows or col>=cols or (row,col) in visited or rooms[row][col]==-1):
                return 
            visited.add((row,col))
            q.append([row,col])

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        dist=0
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                rooms[row][col]=dist
                addRoom(row+1,col)
                addRoom(row-1,col)
                addRoom(row,col+1)
                addRoom(row,col-1)
            dist+=1



                