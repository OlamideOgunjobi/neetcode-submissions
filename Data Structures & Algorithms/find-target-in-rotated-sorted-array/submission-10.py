class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return bs(start, mid-1)
            elif target > nums[mid]:
                return bs(mid+1, end)

        def helper(start, end):

            if start > end:
                return -1

            if nums[start] < nums[end]:
                return bs(start, end)

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:   # left side sorted
                if target < nums[mid] and target >= nums[start]:
                    return helper(start, mid-1)
                else:
                    return helper(mid+1, end)
            elif nums[mid] <= nums[end]:     # right side sorted
                if target > nums[mid] and target <= nums[end]:
                    return helper(mid+1, end)
                else:
                    return helper(start, mid-1)


        return helper(0, len(nums)-1)