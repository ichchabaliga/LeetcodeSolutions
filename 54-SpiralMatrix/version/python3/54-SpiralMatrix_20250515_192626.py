# Last updated: 15/05/2025, 19:26:26
# use boundaries
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols=len(matrix),len(matrix[0])
        left,top=0,0
        bottom,right=rows-1,cols-1
        result=[]
        while len(result)!=rows*cols:
            for i in range(left,right+1):
                result.append(matrix[top][i])
                
            for i in range(top+1,bottom+1):
                result.append(matrix[i][right])

            if top!=bottom:
                for i in range(right-1,left-1,-1):
                    result.append(matrix[bottom][i])

            if left!=right:
                for i in range(bottom-1,top,-1):
                    result.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        return result


            



        