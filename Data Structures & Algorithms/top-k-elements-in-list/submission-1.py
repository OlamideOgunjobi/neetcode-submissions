import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}    # [key:num, val:frequency]
        for num in nums:    # O(n)
            my_dict[num] = my_dict.get(num, 0) + 1
    
        
        my_heap = []    # heap is stored as an array

        for key, value in my_dict.items():
            heapq.heappush(my_heap, (-1 * value, key))  # inserting into the heap

        result = []
        for i in range(k):
            result.append(my_heap[0][1])
            del my_heap[0]
            heapq.heapify(my_heap)

        return result