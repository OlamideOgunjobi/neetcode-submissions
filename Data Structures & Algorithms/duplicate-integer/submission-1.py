class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_nums = []
        for num in nums:
            if num in new_nums:
                return True # returns true if num is in the new list
            new_nums.append(num) # if num is not in new set then it appends num into it

        return False