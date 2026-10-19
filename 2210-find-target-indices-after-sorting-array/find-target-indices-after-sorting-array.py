class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        first=low

        low,high=0,n-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<=target:
                low=mid+1
            else:
                high=mid-1
        last=high
        if first>last:
            return[]
        return list(range(first,last+1))