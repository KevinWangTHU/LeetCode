class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        # use b to move the carry
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else (-1 ^ mask) | a

    def getSum_myself(self, a, b):
        max = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        carry = 0
        base = 1
        ans = 0
        while base < mask:
            cur_a, cur_b = a & base, b & base
            cur = cur_a ^ cur_b ^ carry
            carry = cur_a & cur_b | cur_a & carry | cur_b & carry
            ans = ans | cur
            carry <<= 1
            base <<= 1

        return ans if ans <= max else (-1 ^ mask) | ans

s = Solution()
print s.getSum_myself(1, -1)
