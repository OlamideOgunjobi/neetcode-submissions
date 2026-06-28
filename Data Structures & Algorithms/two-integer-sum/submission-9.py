class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # subtract curr val from target val to get expected_val
        # use a dictionary to find expected_val


        expected_dict = dict()

        # O(n)
        for index, num in enumerate(nums):
            expected_val = target - num

            if expected_val in expected_dict:
                return [expected_dict[expected_val], index]
            
            expected_dict[num] = index