class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ispal = {}
        for i in xrange(len(s)):
            ispal[(i, i)] = True
            for j in xrange(1, min(i+1, len(s)-i)):
                if s[i-j] != s[i+j]:
                    break
                ispal[(i-j, i+j)] = True
            for j in xrange(min(i, len(s)-i)):
                if s[i-j-1] != s[i+j]:
                    break
                ispal[(i-j-1, i+j)] = True

        def part(l):  # s[l:]
            if l == len(s):
                return [[]]
            return [[s[l:k+1]]+succ for k in range(l, len(s)) if (l, k) in ispal for succ in part(k+1)]

        return part(0)
s=Solution()
print s.partition("efe")
