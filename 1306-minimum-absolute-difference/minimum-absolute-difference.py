class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort() #sorting 
        ans=[]
        min_diffr=float("inf")
        # first loop to find the minimum diffr exist
        for j in range(len(arr)-1): 
            diffr=arr[j+1]-arr[j]
            min_diffr=min(min_diffr,diffr)

        #secound loop to find the pair of minimum sum
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min_diffr:
                ans.append([arr[i],arr[i+1]])
        return ans 
            
