class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # use a set to store all possible operations
        # use stack to store the numbers (stack should only have one value left, the final result)
        # int() truncates towards zero

        operations = ['+', '-', '*', '/']
        operations = set(operations)

        results = []

        for val in tokens:
            if val in operations:
                b = int(results.pop())
                a = int(results.pop())

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