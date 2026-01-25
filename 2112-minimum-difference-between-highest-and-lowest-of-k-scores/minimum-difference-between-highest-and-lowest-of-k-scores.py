class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)<=1 and k==1:
            return 0
        num=sorted(nums)
        i=0
        diffr=[]
        for j in range(len(num)):
            if j-i+1==k:
                diffr.append(num[j]-num[i])
                i+=1
        return min(diffr)

