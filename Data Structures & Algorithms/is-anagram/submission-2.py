class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s != t:
            return False
        return True
        # if len(s) != len(t):
        #     return False
        # while len(s) > 0:
        #     if s.pop() != t.pop():
        #         return False
        # return True
        