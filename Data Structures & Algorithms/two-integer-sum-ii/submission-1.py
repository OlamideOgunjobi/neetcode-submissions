class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted(list(set(numbers)))

        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                return [numbers.index(numbers[i])+1, numbers.index(target - numbers[i])+1]