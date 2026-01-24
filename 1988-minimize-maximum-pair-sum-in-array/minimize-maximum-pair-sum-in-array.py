class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first sorted the nums 
        num=sorted(nums)
        # apply two pointer 
        i,j=0,len(num)-1
        # empty list for storing the pairs sum
        ans=[]
        while i<j: 
            ans.append(num[i]+num[j])
            i+=1
            j-=1
        return max(ans) # returning the minimize maximum pair sum 

