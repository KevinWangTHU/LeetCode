class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = dict()
        head, tail, maxlen = 0, 0, 0
        while True:
            while tail < len(s) and s[tail] not in h:
                h[s[tail]] = True
                tail += 1
            if tail - head > maxlen:
                maxlen = tail - head
            if tail == len(s):
                return maxlen
            while s[head] != s[tail]:
                del h[s[head]]
                head += 1
            del h[s[head]]
            head += 1


s = Solution()
print s.lengthOfLongestSubstring("abcabcbb")


