class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or strs == []:
            return ""
        prefix = ""
        count = 0
        minlen = 100000
        for s in strs:
            if minlen > len(s):
                minlen = len(s)
        while count < minlen:
            for i in range(1, len(strs)):
                if not strs[i][count] == strs[0][count]:
                    return prefix
            prefix += strs[0][count]
            count += 1
        return prefix
