class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_arr = ""
        
        for val in s:
            if val.isalpha() or val.isnumeric():
                new_arr += val

        left = 0
        right = len(new_arr) - 1
        while (left < right):

            if new_arr[left].lower() != new_arr[right].lower():
                return False

            left += 1
            right -= 1

        return True