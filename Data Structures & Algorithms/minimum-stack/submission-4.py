class MinStack:

    # stack implementation

    def __init__(self):

        # create an array to store all values pushed
        # create an array to keep track of the minimin value

        self.val_arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        # append the value into val_arr
        # if the min_arr is empty of the value being pushed is less than the value at the end, append

        self.val_arr.append(val)
        if len(self.min_arr) == 0 or val <= self.min_arr[-1]:
            self.min_arr.append(val)

    def pop(self) -> None:

        # if val_arr is not empty
            # remove the last value from val_arr
            # check if the value removed is the current min val in min_arr, if yes remove it
        if len(self.val_arr) > 0: 
            check_val = self.val_arr.pop()
            if check_val == self.min_arr[-1]:
                self.min_arr.pop()

    def top(self) -> int:
        # return the value at the top of the stack

        return self.val_arr[-1]

    def getMin(self) -> int:
        # return the value at the top of min_arr

        return self.min_arr[-1]
