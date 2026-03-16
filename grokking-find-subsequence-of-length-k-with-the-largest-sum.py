import heapq

def max_subsequence(nums, k):
    min_heap = []
    
    for i, num in enumerate(nums):
        heapq.heappush(min_heap, (num, i))
        
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    min_heap.sort(key=lambda x: x[1])
    
    return [num for num, index in min_heap]
          
