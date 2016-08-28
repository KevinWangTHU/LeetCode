# Another use of lower bound binary search.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l, r = 0, len(citations)-1
        while l <= r:
            m = (l+r) // 2
            if len(citations)-m-1 >= citations[m]:
                l = m + 1
            else:
                r = m - 1
        return len(citations) - l
