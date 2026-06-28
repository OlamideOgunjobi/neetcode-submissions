class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # a value can either be the start of the sequence or part of the sequence
        # convert the arr into a set since duplicates dont matter
        # iterate through the array and check if each element has a left neighbor
        # if it does then skip, if it doesn't then it is the start of a sequence
        # if it has right neighbors, then the sequence continues, if not it ends
    

        changed_nums = set(nums)    # O(n)
        longest_seq = 0
        count = 0

        # O(n): not fully understood why
        for num in changed_nums:
            if (num - 1) not in changed_nums:   # start of a sequence
                count = 1

                while (num + 1) in changed_nums:
                    num += 1
                    count += 1

                if longest_seq < count:
                    longest_seq = count

        return longest_seq