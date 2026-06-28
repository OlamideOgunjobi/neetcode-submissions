class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        left = 0
        right = 0

        length = 0
        chars = dict()


        while right < len(s):

            if s[right] in chars:
                chars[s[right]] += 1
            else:
                chars[s[right]] = 1


            if (right - left + 1) - max(chars.values()) <= k:
                length = max(length, sum(chars.values()))
            else:
                chars[s[left]] -= 1
                left += 1

            right += 1
                
        return length


        # while right < len(s):
        #     if s[right] in chars:
        #         chars[s[right]] += 1
        #     else:
        #         chars[s[right]] = 1


        #     if (right - left + 1) - max(chars.values()) <= k:
        #         length = max(length, sum(chars.values()))
        #         print(f"length: {length}")
        #     else:
        #         while (right - left + 1) - max(chars.values()) > k:
        #             chars[s[left]] -= 1
        #             left += 1

                
            
        #     right += 1

        return length