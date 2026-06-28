class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return

        stack = []  # 2d array storing the [temp, index]
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = abs(i - stackIdx)
            stack.append([t, i])

        return result
        # for i in range(len(temperatures)):
        #     if len(my_stack) == 0:
        #         my_stack.append(temperatures[i])
        #         continue

        #     while temperatures[i] > my_stack[-1]:
        #         result[temperatures.index(temperatures[i])] = abs(temperatures.index(temperatures[i]) - temperatures.index(my_stack.pop()))
        #         if len(my_stack) == 0:
        #             my_stack.append(temperatures[i])
        #             continue

        #     my_stack.append(temperatures[i])

        # return result