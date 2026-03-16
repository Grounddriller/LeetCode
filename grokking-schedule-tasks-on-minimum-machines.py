import heapq

def minimum_machines(tasks):
    if not tasks:
        return 0
        
    tasks.sort(key=lambda x: x[0])
    
    min_heap = []
    
    heapq.heappush(min_heap, tasks[0][1])
    
    for i in range(1, len(tasks)):
        start, end = tasks[i]
        
        if start >= min_heap[0]:
            heapq.heappop(min_heap)
            
        heapq.heappush(min_heap, end)
    
    return len(min_heap)
