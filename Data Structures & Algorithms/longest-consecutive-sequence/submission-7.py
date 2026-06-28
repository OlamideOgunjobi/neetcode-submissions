class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        # count is set to 1 to account for the first value in the sequence
        # if confused, try manually testing count as 0 and see result
        count = 1
        longest_count = 0

        for num in nums:
            # if it has a predecessor, it is not the start of a sequence
            # so skip and find the predecessor
            if num - 1 in nums:
                continue

            # if it is the predecessor:
            while True:
                # if there is an immediate successor continue the iteration on that sequence and increment
                if num + 1 in nums:
                    count += 1
                    num += 1
                # if there is no immediate successor, end the sequence and update 'longest_count' if necessary
                else:
                    if longest_count < count:
                        longest_count = count
                    count = 1
                    break

        # return the length of the longest sequence
        return longest_count

