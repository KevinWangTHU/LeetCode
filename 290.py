class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def toList(l):
            d = {}
            count = 0
            ret = []
            for item in l:
                if item not in d:
                    d[item] = count
                    count += 1
                ret.append(d[item])
            return ret
        l1, l2 = toList(pattern), toList(str.split())
        return True if l1 == l2 else False

s=Solution()
s.wordPattern("abba", "dog cat cat fish")
