class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        array = []

        for para in s:
            if para not in closing:
                array.append(para)
            else:
                if len(array) == 0:
                    return False
                else:
                    if opening[closing.index(para)] == array[-1]:
                        del array[-1]
                    else:
                        return False



        return len(array) == 0