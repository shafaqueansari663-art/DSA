class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result=[]
        for hour in range(12):
            for minute in range(60):
                if(bin(hour).count('1')+bin(minute).count('1'))==turnedOn:
                    time=str(hour)+":"+str(minute).zfill(2)
                    result.append(time)
        return result
        