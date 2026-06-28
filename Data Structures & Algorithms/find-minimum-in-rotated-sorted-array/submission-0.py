class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def helper(start, end):

            # if nums[left] < nums[right], no shifting has occured / shifted back to original spot
            # if any significant shifting had happened, the left would definitely be greater than the start


            if nums[start] < nums[end] or start == end:
                return nums[start]

            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                return helper(mid+1, end)
            elif nums[mid] < nums[start]:
                return helper(start, mid)

            return nums[left]

        return helper(0, len(nums)-1)

            