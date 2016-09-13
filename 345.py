class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        d = {}
        s = [c for c in s]
        for v in vowels:
            d[v] = True
        i, j = 0, len(s)-1
        while True:
            while i < len(s) and s[i] not in d:
                i += 1
            while j >= 0 and s[j] not in d:
                j -= 1
            if i > j:
                break
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)

s=Solution()
print s.reverseVowels("HellO")
