class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return

        my_stack = []
        signs = ['+', '-', '*', '/']
        for elem in tokens:
            if not elem in signs:
                my_stack.append(int(elem))
            else:
                b = my_stack.pop()
                a = my_stack.pop()
                if elem == '+':
                    result = a + b
                elif elem == '-':
                    result = a - b
                elif elem == '*':
                    result = a * b
                elif elem == '/':
                    result = int(a / b)

                my_stack.append(result)

        return my_stack[0]