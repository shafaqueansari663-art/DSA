class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m=len(mat)
        n=len(mat[0])
        #creating an empty arrray to store the count of 1 in row colm
        row_count=[0]*m
        colm_count=[0]*n
        #counting 1
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    row_count[i]+=1
                    colm_count[j]+=1
        #checking special cases
        special=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and row_count[i]==1 and colm_count[j]==1:
                    special+=1
        return special
        