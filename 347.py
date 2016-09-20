class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        l = []
        for key in d.keys():
            l.append((key, d[key]))
        l.sort(key = lambda x:x[1], reverse=True)
        return [l[i][0] for i in range(k)]
s=Solution()
print s.topKFrequent([3,2,2,1,1,1],2)
