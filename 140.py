class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        f, g = [[]], [True]
        for i in range(1, len(s)+1):
            flag = False
            cur = []
            for w in wordDict:
                if s[i-len(w):i] == w:
                    cur.append(w)
                    flag |= g[i-len(w)]
            g.append(flag)
            f.append(cur)

        def buildpath(i):
            if i == 0:
                return [""]
            return [prev + " " + cur for cur in f[i] for prev in buildpath(i-len(cur)) if i >= len(cur)]
        return [s[1:] for s in buildpath(len(s))] if g[len(s)] else []
s=Solution()
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
