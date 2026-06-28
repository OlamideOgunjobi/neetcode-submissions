class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # use a stack

        my_stack = []

        for tok in tokens:  # O(n)
            if tok not in ["+", "-", "*", "/"]: # if it is a number, add to the stack
                my_stack.append(int(tok))
            else:
                second = my_stack.pop()
                first = my_stack.pop()

                if tok == "+":
                    my_stack.append(first + second)
                elif tok == "-":
                    my_stack.append(first - second)
                elif tok == "*":
                    my_stack.append(first * second)
                elif tok == "/":
                    my_stack.append(int(first / second))

        return my_stack[0]