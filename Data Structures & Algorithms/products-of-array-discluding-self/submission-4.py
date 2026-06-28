class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # create an array to store the prefix and suffix product
        # calculate the prefix product for each element
        # calculate the suffix product for each element
        # create a result array and calculate the product of prefix and suffix for each element

        prefix = []
        suffix = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1] * prefix[i-1])

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                suffix[i] = nums[i+1] * suffix[i+1]

        result = [1] * len(nums)
        for i in range(len(prefix)):
            result[i] = prefix[i] * suffix[i]


        return result