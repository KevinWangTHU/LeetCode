class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(reverse=True, cmp=lambda x,y: 1 if x[0] > y[0] or x[0] == y[0] and x[1] < y[1] else -1)
        ans = [0] * len(people)
        for i, p in enumerate(people):
            for j in range(i-1, p[1]-1, -1):
                ans[j+1] = ans[j]
            ans[p[1]] = p
        return ans
s=Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
