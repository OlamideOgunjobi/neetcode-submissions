class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        start, end = 0, len(nums) - 1

        prefix, suffix = [], []
        pre_val, suf_val = 1, 1
        # prefix loop
        for i in range(len(nums)):
            if i == start:
                prefix.append(pre_val)
                continue

            pre_val *= nums[i-1]
            prefix.append(pre_val)

        for i in range(len(nums) - 1, -1, -1):
            if i == end:
                suffix.append(suf_val)
                continue
            
            suf_val *= nums[i+1]
            suffix.append(suf_val)

        result = []
        for i in range(len(suffix)):
            result.append(suffix[len(suffix) - 1 - i] * prefix[i])

        return result