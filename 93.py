class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def search(depth, idx, cur):
            if depth == 4:
                if idx == len(s):
                    ans.append(".".join(cur))
                return
            if idx == len(s):
                return
            if s[idx] == "0":
                cur.append("0")
                search(depth+1, idx+1, cur)
                cur.pop()
            else:
                for end in range(idx+1, min(idx+3, len(s))+1):
                    if int(s[idx:end]) <= 255:
                        cur.append(s[idx:end])
                        search(depth+1, end, cur)
                        cur.pop()
        search(0, 0, [])
        return ans
s=Solution()
print s.restoreIpAddresses("25525511135")
