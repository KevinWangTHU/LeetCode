class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = num
        remain = n
        ans = []

        letters = ["I", "V", "X", "L", "C", "D", "M"]
        nums = [1, 5, 10, 50, 100, 500, 1000]

        for i in range(6, -1, -1):
            num = nums[i]
            letter = letters[i]
            if 4*num > remain >= num:
                ans.append(letter * (remain/num))
                remain -= remain/num * num
            if letter in ["D", "M"]:
                subtract = num - 100
                l = "C"
            elif letter in ["L", "C"]:
                subtract = num - 10
                l = "X"
            elif letter in ["V", "X"]:
                subtract = num - 1
                l = "I"
            else:
                subtract = 1000000
            if remain >= subtract:
                remain -= subtract
                ans.append(l)
                ans.append(letter)
        return "".join(ans)

s = Solution()
print s.intToRoman(19)
