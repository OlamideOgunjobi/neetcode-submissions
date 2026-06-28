class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        if not s:
            return length

        check = ""
        
        for c in s:
            if c in check:
                if len(check) > length:
                    length = len(check)
                check = check[check.index(c)+1:]
            check += c

        if len(check) > length:
            length = len(check)
        return length