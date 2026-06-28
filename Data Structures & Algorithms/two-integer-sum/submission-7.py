class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup_dict = {}

        
        for i,val in enumerate(nums):    # O(n)
            sub_val = target - val
            if sub_val in lookup_dict:  # O(1)
                return [lookup_dict[sub_val], i]
            lookup_dict[val] = i    # store values as the key and the value of the key being the index in array            