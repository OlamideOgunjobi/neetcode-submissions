class MinStack:

    def __init__(self):
        self.myArray = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.myArray.append(val)

        # pushing the min value to the end of the array
        if not self.minVal or val <= self.minVal[-1]:
            self.minVal.append(val)


    def pop(self) -> None:
        val = self.myArray[-1]
        if val == self.minVal[-1]:
            del self.minVal[-1]
        del self.myArray[-1]


    def top(self) -> int:
        return self.myArray[-1]

    def getMin(self) -> int:
        return self.minVal[-1]