class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = dict()

        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1

        my_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

        keys_list = [item[0] for item in my_dict]

        return keys_list[:k]
        