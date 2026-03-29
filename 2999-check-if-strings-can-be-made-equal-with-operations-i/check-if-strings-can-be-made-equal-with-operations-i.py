class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #checking at index 0 and 2
        num1= sorted([s1[0],s1[2]])
        num2=sorted([s2[0],s2[2]]) 
        # checking at index 1 and 3
        num3=sorted([s1[1],s1[3]])
        num4=sorted([s2[1],s2[3]])
        
        return num1==num2 and num3==num4

        