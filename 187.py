class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        # A 00 C 01 G 10 T 11
        d = {"A": 0, "C": 1, "G": 2, "T": 3}
        ans = []
        h = {}
        prev = sum([d[s[i]] * 4 ** (9-i) for i in range(10)])
        h[prev] = 1
        for j in range(10, len(s)):
            prev %= 4 ** 9
            prev = 4 * prev + d[s[j]]
            if prev in h and h[prev] == 1:
                ans += s[j-9:j+1],
                h[prev] += 1
            elif prev not in h:
                h[prev] = 1
        return ans
