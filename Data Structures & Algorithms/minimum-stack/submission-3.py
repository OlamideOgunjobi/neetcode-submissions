class MinStack:

    def __init__(self):
        self.my_array = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.my_array.append(val)   # O(1)
        if len(self.min_val) == 0 or val <= self.min_val[-1]:
            self.min_val.append(val)

    def pop(self) -> None:
        if len(self.my_array) != 0:
            val = self.my_array[-1]
            del self.my_array[-1]    # O(1)
            if val == self.min_val[-1]:
                del self.min_val[-1]

    def top(self) -> int:
        return self.my_array[-1] # O(1)

    def getMin(self) -> int:
        return self.min_val[-1]
        
