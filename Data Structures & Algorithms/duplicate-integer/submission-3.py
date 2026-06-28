class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # create a set, since it stores only unique numbers
        # check if that value is in set

        dups = set()

        for n in nums:
            if n in dups:
                return True
            dups.add(n)

        return False