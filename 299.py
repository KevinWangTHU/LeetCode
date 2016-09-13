class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secCnt = [0] * 10
        gueCnt = [0] * 10
        bull, cow = 0, 0
        for i in range(len(secret)):
            secCnt[ord(secret[i]) - 48] += 1
            gueCnt[ord(guess[i]) - 48] += 1
            if secret[i] == guess[i]:
                bull += 1
        for i in range(10):
            cow += min(secCnt[i], gueCnt[i])
        cow -= bull
        return str(bull)+"A"+str(cow)+"B"
s=Solution()
print s.getHint("1807", "1999")
