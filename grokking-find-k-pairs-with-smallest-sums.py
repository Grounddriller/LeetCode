from heapq import *

def k_smallest_pairs(list1, list2, k):
    result = []
    
    if not list1 or not list2 or k == 0:
        return result

    min_heap = []
    
    for i in range(min(k, len(list1))):
        heappush(min_heap, (list1[i] + list2[0], i, 0))
        
    while min_heap and len(result) < k:
        pair_sum, i, j = heappop(min_heap)
        
        result.append([list1[i], list2[j]])
        
        if j + 1 < len(list2):
            heappush(min_heap, (list1[i] + list2[j + 1], i, j + 1))

    return result
    
