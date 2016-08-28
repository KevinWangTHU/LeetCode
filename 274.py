class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        citations.append(0)
        for i, cite in enumerate(citations):
            if i >= cite:
                break
        return i
