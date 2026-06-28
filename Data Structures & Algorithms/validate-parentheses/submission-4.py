class Solution:
    def isValid(self, s: str) -> bool:
        
        opening_stack = []
        matching_dict = {")":"(", "}":"{", "]":"["}

        if (len(s) % 2) != 0:   # not even so not everything mathces
            return False

        for val in s:
            if val not in matching_dict.keys():  # it is an opening
                opening_stack.append(val)
            else:   # it is a closing
                if not len(opening_stack):
                    return False
                elif matching_dict[val] != opening_stack[-1]: # if the value(opening) is not at the end of stack, not matching
                    return False
                else:
                    del opening_stack[-1]
                    continue

        if len(opening_stack) != 0: # if not zero then not all matched
            return False

        return True
