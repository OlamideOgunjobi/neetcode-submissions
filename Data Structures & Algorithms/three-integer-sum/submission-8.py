class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # list is already sorted
        # traverse through the list for the first values
        # for each iteration, use two pointer method to find the second and third value
        # no need to go to the back of the first value with the left pointer, this is unecessary and would cause duplicates
        # when a combination is found, insert into output array

        nums.sort()

        result = []

        visited = set()

        # O(n)
        for i in range(len(nums)):
            
            if nums[i] in visited:  # skips duplicates
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    dup = nums[left]
                    while dup == nums[left] and left < right:
                        left += 1

                    dup = nums[right]
                    while dup == nums[right] and left < right:
                        right -= 1
                        
                elif val < 0:
                    dup = nums[left]
                    while dup == nums[left] and left < right:
                        left += 1
                elif val > 0:
                    dup = nums[right]
                    while dup == nums[right] and left < right:
                        right -= 1

            visited.add(nums[i])



        return result