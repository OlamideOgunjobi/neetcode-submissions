class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # use a set to store all possible operations
        # use stack to store the numbers (stack should only have one value left, the final result)
        # if the current value is an operation, perform the operation
            #  pop the first value, this should be b
            #  pop the second value, this should be a
            # int() truncates towards zero for the division operation
        # if the current value is a number, append to the end of the list (convert to an int first)
        # return index 0 since this should be the answer
        


        operations = ['+', '-', '*', '/']
        operations = set(operations)

        results = []

        for val in tokens:
            if val in operations:
                b = results.pop()
                a = results.pop()

                if val == '+':
                    results.append(a+b)
                elif val == '-':
                    results.append(a-b)
                elif val == '*':
                    results.append(a*b)
                elif val == '/':
                    results.append(int(a/b))
            else:
                results.append(int(val))

        return results[0]