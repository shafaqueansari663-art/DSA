class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count2=0
        count1=0
        for i in range(len(s)):
            #0101
            if s[i]!=str(i%2):
                count1+=1
            #1010
            if s[i] !=str((i+1)%2):
                count2+=1
        return min(count1,count2)
