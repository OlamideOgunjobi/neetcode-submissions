class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort() # sorting the array

        for i, num_1 in enumerate(nums):
            # exits if the first number is not negative or zero
            # becuase then, in a sorted list, the sum will never add to zero
            if (num_1 > 0):
                break

            # skips if the first value will be a duplicate
            if i > 0 and num_1 == nums[i-1]:
                continue

            # left and right pointers
            left, right = i+1, len(nums) - 1

            # value the pointers have to add up to
            
            while left < right:
                target = num_1 + nums[left] + nums[right]
                if (target) > 0:
                    right -= 1
                elif (target) < 0:
                    left += 1
                else:
                    ans.append([num_1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1


        return ans