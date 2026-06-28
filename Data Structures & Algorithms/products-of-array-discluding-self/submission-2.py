class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # inintialized as 1 because anything multiplied by 1 is itself
        output_array = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                output_array[i] *= nums[j]

        return output_array