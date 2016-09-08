class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        for str1, str2 in map(None, v1, v2):
            num1 = int(str1) if str1 else 0
            num2 = int(str2) if str2 else 0
            if num1 == num2:
                continue
            return 1 if num1 > num2 else -1
        return 0
