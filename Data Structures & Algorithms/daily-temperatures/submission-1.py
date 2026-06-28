class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        # create a stack to store the values
        # create an array to store the resulting differences
        # iterate through the entire list
        # if length > 0 and 

        store_vals = [] # (val, index)

        results = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while len(store_vals) > 0 and store_vals[-1][0] < temperatures[i]:
                    val, index = store_vals.pop()
                    results[index] = i - index
            
            store_vals.append((temperatures[i], i))

        return results