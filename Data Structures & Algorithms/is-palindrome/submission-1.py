class Solution:
    def isPalindrome(self, s: str) -> bool:

        # removing the spaces from a string
        s = s.replace(" ", "")
        s = s.lower()

        partial_s = ""
        for i in range(len(s)):
            if not 64 < ord(s[i].upper()) < 91 and not 47 < ord(s[i].upper()) < 58:
                continue
            partial_s += s[i]

        # reversing a string
        new_s = partial_s[::-1]

        if partial_s == new_s: return True

        return False