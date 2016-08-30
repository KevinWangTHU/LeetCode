class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n % 4 else False

    def canWinNim_stupid(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n <= 3:
            return True
        return self.notLoseNim(n-1) or self.notLoseNim(n-2) \
              or self.notLoseNim(n-3)

    def notLoseNim(self, n):
        if n <= 0:
            return True
        return self.canWinNim(n-1) and self.canWinNim(n-2) \
              and self.canWinNim(n-3)
