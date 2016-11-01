class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        f = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            f[i] = any(f[i-len(w)] for w in wordDict if i-len(w) >= 0 and s[i-len(w):i] == w)
        return f[len(s)]
