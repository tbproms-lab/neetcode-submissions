class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if -first == -second:
                pass
            elif -first > -second:
                new = -first - (-second)
                heapq.heappush(maxHeap, -new)
        
        if len(maxHeap) == 0:
            return 0
        return -maxHeap[0]
            
            
            