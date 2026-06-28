class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #hash set to store values
        duplicate_checker = set()

        for num in nums: # O(n)

            # checks if the valus is already in the set
            if num in duplicate_checker: # O(1)
                return True

            duplicate_checker.add(num)
            

        return False