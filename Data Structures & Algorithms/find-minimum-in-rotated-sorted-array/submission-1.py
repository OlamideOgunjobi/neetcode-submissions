class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        def helper(start, end):

            if start == end or nums[start] < nums[end]:
                return nums[start]

            mid = (start + end) // 2

            if nums[mid] > nums[end]: # (if mid is greater, we can exclude it from the range because it would not be part of the sorted range witht the minimum *We don't need any valu that is not less than another*)
                return helper(mid+1, end)
            else: # nums[mid] < nums[end] (If the mid is left, it is part of the sorted min range, and could possibly be the min so don't exclude)
                return helper(start, mid)


        return helper(0, len(nums)-1)