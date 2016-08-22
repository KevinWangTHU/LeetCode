class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        phones = {"1":"" , "2":"abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" , "7":"pqrs" , "8":"tuv" , "9":"wxyz"}
        ans = [""]
        for d in digits:
            cur = []
            for pre in ans:
                for c in phones[d]:
                    cur.append(pre+c)
            ans = cur
        return ans
