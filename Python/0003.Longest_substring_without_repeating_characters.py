class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        res = 0
        left = 0
        i = 0
        while i < len(s):
            if s[i] not in m:
                m.add(s[i])
                res = max(res, len(m))
                i += 1
            else:
                m.remove(s[left])
                left += 1
        return res
