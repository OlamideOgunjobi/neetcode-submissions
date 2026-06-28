class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 cannot ba a substring of s2 if it has less values in it
        if len(s2) < len(s1):
            return False

        # organize the substring
        s1 = sorted(s1)

        # temp var to organize the sliding values of the
        temp = ""
        
        # size of the window
        sliding_val = len(s1)

        while True:
            if sliding_val > len(s2):
                break

            temp = sorted(s2[ : sliding_val])

            if temp == s1:
                return True


            # cut off the leftmost character
            s2 = s2[1:]

        return False