# Should be able to figure out this solution!
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (D-B) * (C-A)
        area2 = (H-F) * (G-E)
        lowerTop = min(D, H)
        upperBot = max(B, F)
        lefterRight = min(C, G)
        righterLeft = max(A, E)
        overlap = (lefterRight - righterLeft) * (lowerTop - upperBot) \
            if lefterRight > righterLeft and lowerTop > upperBot else 0

        return area1 + area2 - overlap
