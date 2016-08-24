class Solution(object):
    def combinationSum2_clean(self, candidates, target):
        def dfs(candidates, start, target):
            if target == 0:
                return [[]]
            res = [] # init: do not take
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    # only take the current one
                    continue
                if candidates[i] > target:
                    break
                for r in dfs(candidates, i+1, target-candidates[i]):
                    res.append(r+[candidates[i]])
            return res
        candidates.sort()
        return dfs(candidates, 0, target)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def f3(seq):
            # Not order preserving
            keys = {}
            for e in seq:
                keys[e] = 1
            return keys.keys()

        candidates.sort()
        d = {}
        for item in candidates:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        candidates = f3(candidates)

        def dfs(candidates, target, idx):
            print target
            if target == 0:
                return [[]]
            if idx < 0:
                return None
            x = candidates[idx]
            ans = []
            solved = False
            for i in range(min(d[x], target//x) + 1):
                anslist = dfs(candidates, target-i*x, idx-1)
                if anslist:
                    solved = True
                    for j in range(len(anslist)):
                        anslist[j].extend([x]*i)
                    ans.extend(anslist)

            if solved:
                return ans
            else:
                return None
        ans = dfs(candidates, target, len(candidates)-1)
        return ans if ans else []
