class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # use a left and right pointer to compare each character in the string
        # make sure to check for punctuations first and move the pointer if needed
        # if the two pointers equal each other, move both; else return false
        # you want to do this while the left is less than the right, because their path would mirror each other so no need to keep going (anything past that point should be identical)
        # increment the left and right pointer accordingly

        left = 0
        right = len(s) - 1


        # O(n)
        while left < right:

            # skipping punctuations
            while (not s[left].isalnum()) and left < right:
                left += 1
            
            while (not s[right].isalnum()) and left < right:
                right -= 1

            # end if the two characters don't equal each other
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1


        return True