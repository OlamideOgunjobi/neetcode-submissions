class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # array in ascending order
        # check middle, if equal, return index
        # if the target is less than middle, check the left side
        # if the target is greater than middle, check the right side

        def binary_search(arr: List[int], start: int, end: int, target: int) -> int:

            
            if start > end:
                return -1

            middle = (start + end) // 2

            print(middle)
            if arr[middle] == target:
                return middle
            elif target < arr[middle]:
                return binary_search(arr, start, middle-1, target)
            elif target > arr[middle]:
                return binary_search(arr, middle+1, end, target)


        return binary_search(nums, 0, len(nums)-1, target)
