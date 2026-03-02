class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        end_zeros=[]
        #counting the no of zerospresent in rows backward 
        for row in grid:
            count=0
            for val in reversed(row):
                if val==0:
                    count+=1
                else:
                    break
            end_zeros.append(count)

        swap=0
        
        for i in range(n):
            needed=n-i-1
            j=i
            while j <n and end_zeros[j]< needed:
                j+=1
            if j==n:
                return -1
            while j >i:
                end_zeros[j],end_zeros[j-1]=end_zeros[j-1],end_zeros[j]
                swap +=1
                j-=1
        return swap
