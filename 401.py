class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def searchH(hour, value, total):
            if hour == 0:
                if total < 12:
                    h.append(total)
                return
            if value+1 == hour:
                total += 2**value * 2 - 1
                if total < 12:
                    h.append(total)
                return
            # minute < value+1, minute > 0
            searchH(hour, value-1, total)
            searchH(hour-1, value-1, total+2**(value))

        def searchM(minute, value, total):
            if minute == 0:
                if total < 60:
                    m.append(total)
                return
            if value+1 == minute:
                total += 2**value * 2 - 1
                if total < 60:
                    m.append(total)
                return
            # minute < value+1, minute > 0
            searchM(minute, value-1, total)
            searchM(minute-1, value-1, total+2**(value))
        ans = []
        for hour in range(max(0, num-6), min(num+1, 4)):
            h, m = [], []
            minute = num - hour
            searchH(hour, 3, 0)
            searchM(minute, 5, 0)
            ans.extend([str(hour)+":"+str(minute) if minute > 9 else str(hour)+":0"+str(minute) for hour in h for minute in m])
        return ans

s = Solution()
print s.readBinaryWatch(7)
