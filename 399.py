class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = {}
        for i in range(len(equations)):
            f, t = equations[i]
            val = values[i]
            if f in d:
                d[f].append((t, val))
            else:
                d[f] = [(t, val)]
            if t in d:
                d[t].append((f, 1/val))
            else:
                d[t] = [(f, 1/val)]
        vis = set()
        nums = {}
        group = {}
        groupCount = 0
        def dfs(root, val, groupCount):
            for t, v in d[root]:
                if t not in vis:
                    nums[t] = val / v
                    vis.add(t)
                    group[t] = groupCount
                    dfs(t, nums[t], groupCount)
        for key in d.keys():
            if key not in vis:
                vis.add(key)
                nums[key] = 1.0
                group[key] = groupCount
                dfs(key, 1.0, groupCount)
                groupCount += 1
        ans = []
        for q1, q2 in queries:
            if q1 not in vis or q2 not in vis or group[q1] != group[q2]:
                ans.append(-1.0)
            else:
                ans.append(nums[q1] / nums[q2])
        return ans
s=Solution()
print s.calcEquation([["a","b"],["c","d"]],
                     [1.0,1.0],
                     [["a","c"],["b","d"],["b","a"],["d","c"]])
