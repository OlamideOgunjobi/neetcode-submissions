class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        left = 0
        right = 0

        longest = 0

        while right < len(s):

            if s[right]  in seen:
                longest = max(longest, len(seen))

                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                    
                seen.remove(s[left])
                left += 1
                seen.add(s[right])

            seen.add(s[right])
            longest = max(longest, len(seen))
            right += 1

        return longest
                
