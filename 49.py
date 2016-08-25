class Solution(object):
    def groupAnagrams_slow(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        for s in strs:
            num = 0
            for c in s:
                num += 2**(ord(c)-97)
            if num in table:
                table[num].append(s)
            else:
                table[num] = [s]
        return table.values()

    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            k = tuple(sorted(s))
            d[k] = d.get(k, []) + [s]  # seems this will be slower
        return d.values()
