import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # create a dictionary to store the frequency of occurences
        # create a heap from the values of the dictionaries
        # loop through k times and get the top element from the heap
        # remove the top element and heapify again


        freq = dict()

        # O(n)
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        kv_pair = []
        for key, value in freq.items():
            kv_pair.append((value, key))
            
        heapq.heapify_max(kv_pair) # in-place heap

        result = []

        for i in range(k):
            value, key = heapq.heappop_max(kv_pair)    # inplace popping and heapify, returns value popperd
            result.append(key)

        return result