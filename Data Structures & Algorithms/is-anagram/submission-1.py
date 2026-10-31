class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        have1 = {}
        have2 = {}

        for i in range(len(s)):
            have1[s[i]] = 1 + have1.get(s[i], 0)
            have2[t[i]] = 1 + have2.get(t[i], 0)

        if have1 == have2:
            return True
        else:
            return False