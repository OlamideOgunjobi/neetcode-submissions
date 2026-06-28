class Solution:
    def isValid(self, s: str) -> bool:
        
        # use dictionary to match braces
        # use a list following the implementation of a stack, LIFO
        # store the opening braces in an array and check if the closed braces you are on is for the opening brace at the top
        # if the closing brace is not for the opening brace at the top, return false
        # if the stack is not empty, return false

        opening = {")": "(", "}": "{", "]": "["}
        seen = []

        for brace in s:

            if brace in opening.values():
                seen.append(brace)
            else:
                if len(seen) != 0 and opening[brace] == seen[-1]:
                    seen.pop()
                else:
                    return False


        if len(seen) != 0:
            return False

        return True