def seq(height, type="inc"):
    if type == "inc":
        iseq = [(height[0], 0)]
        for i in range(1, len(height)):
            if height[i] > iseq[-1][0]:
                iseq.append((height[i], i))
        return iseq
    else:
        dseq = [(height[-1], len(height)-1)]
        for j in range(len(height)-2, -1, -1):
            if height[j] > dseq[-1][0]:
                dseq.append((height[j], j))
        return dseq

# Stupid nlogn
def maxA(height):
    if len(height) < 2:
        return 0
    if len(height) == 2:
        return min(height)

    med = len(height) // 2
    leftA = maxA(height[:med])
    rightA = maxA(height[med:])

    leftFil = seq(height[:med], "inc")
    rightFil = seq(height[med:], "dec")

    i, j = 0, 0
    # left - i
    # right - j + med
    maxarea = 0
    while i < len(leftFil) and j < len(rightFil):
        if leftFil[i][0] < rightFil[j][0]:
            area = leftFil[i][0] * (rightFil[j][1]+med - leftFil[i][1])
            i += 1
        else:
            area = rightFil[j][0] * (rightFil[j][1]+med - leftFil[i][1])
            j += 1
        if area > maxarea:
            maxarea = area
    return max(leftA, rightA, maxarea)

def maxB(height):
    if len(height) < 2:
        return 0
    if len(height) == 2:
        return min(height)

    maxindex = height.index(max(height))
    leftFil = seq(height, "inc")
    rightFil = seq(height, "dec")

    i, j = 0, 0
    maxarea = 0
    while i < len(leftFil) and j < len(rightFil):
        if leftFil[i][0] < rightFil[j][0]:
            area = leftFil[i][0] * (rightFil[j][1] - leftFil[i][1])
            i += 1
        else:
            area = rightFil[j][0] * (rightFil[j][1] - leftFil[i][1])
            j += 1
        if area > maxarea:
            maxarea = area
    return maxarea

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return maxB(height)

print maxB([3,4,5,3,1,3,5,7,1,4,6,1])
