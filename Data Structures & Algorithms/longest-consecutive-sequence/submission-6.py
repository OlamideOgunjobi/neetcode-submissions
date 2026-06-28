class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        count = 1
        longest_count = 0

        for num in nums:
            # if it has a predecessor, it is not the start of a sequence
            # so skip and find the predecessor
            if num - 1 in nums:
                continue

            temp = num
            while True:
                # if it is the predecessor:
                if num + 1 in nums:
                    count += 1
                    num += 1
                else:
                    if longest_count < count:
                        longest_count = count
                    count = 1
                    break


        return longest_count

