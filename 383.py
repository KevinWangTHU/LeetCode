class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def count(s):
            nums = [0] * 26
            for c in s:
                nums[ord(c)-97] += 1
            return nums
        ransomNums = count(ransomNote)
        magazineNums = count(magazine)
        for i in range(26):
            if ransomNums[i] > magazineNums[i]:
                return False
        return True
