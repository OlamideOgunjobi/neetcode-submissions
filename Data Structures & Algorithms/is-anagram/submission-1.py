class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        a.sort()

        b = list(t)
        b.sort()

        if len(s) != len(t):
            return False
        elif ''.join(a) == ''.join(b):
            return True

        return False            
