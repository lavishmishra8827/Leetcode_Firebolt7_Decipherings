class Solution:
    def convert_single_index_to_row_column(self,n,index,matrix):
        print(index//n,index%n)
        return matrix[index//n][index%n]
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        def bin_search(low,high):
            if low>high:
                return False
            mid=(low+high)//2
            mid_value=self.convert_single_index_to_row_column(n,mid,matrix)
            if mid_value==target:
                return True
            if mid_value>target:
                return bin_search(low,mid-1)
            return bin_search(mid+1,high)
        return bin_search(0,m*n-1)
sol=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#target = 13
matrix=[[1]]
target=1
print(sol.searchMatrix(matrix,target))
