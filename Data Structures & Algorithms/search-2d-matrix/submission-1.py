class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
       # flatten the matrix

        rows = len(matrix)
        cols = len(matrix[0])

        def helper(left, right):

            if left > right:
                return False

            middle = (left + right) // 2
            val = matrix[middle // cols][middle % cols]
            
            if val == target:
                return True
            elif target < val:
                return helper(left, middle-1)
            elif target > val:
                return helper(middle+1, right)


        return helper(0, rows * cols - 1)
