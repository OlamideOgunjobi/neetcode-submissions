class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort the given list
        # traverse through the list for the first values
        # for each iteration, use two pointer method to find the second and third value
        # no need to go to the back of the first value with the left pointer, this is unecessary and would cause duplicates
        # when a combination is found, insert into output array
        # always increment each value to ensure it is different and not a duplicate from the one it was currently just on

        nums.sort()

        result = []

        visited = set()

        # O(n)
        for i in range(len(nums)):
            
            if i > 0 and nums[i-1] == nums[i]:  # skips duplicates
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while nums[left-1] == nums[left] and left < right:
                        left += 1

                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                        
                elif val < 0:
                    left += 1
                elif val > 0:
                    right -= 1

            visited.add(nums[i])



        return result