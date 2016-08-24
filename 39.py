class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(candidates, start, target):
            if target == 0:
                return [[]]
            res = []
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                for k in range(1, target//candidates[i]+1):
                    for r in dfs(candidates, i+1, target-candidates[i]*k):
                        res.append(r + [candidates[i]]*k)
            return res
        candidates.sort()
        return dfs(candidates, 0, target)
