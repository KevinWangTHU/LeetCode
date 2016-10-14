class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        net = [gas[i] - cost[i] for i in range(len(gas))]
        minIdx = net.index(min(net))
        curIdx = minIdx
        curNeed = -net[curIdx]
        count = 0
        MIN = curNeed
        ans = curIdx
        while count < len(gas):
            count += 1
            curIdx = curIdx - 1 if curIdx > 0 else len(gas)-1
            curNeed = curNeed-net[curIdx]
            if curNeed < MIN:
                MIN = curNeed
                ans = curIdx
        return ans
