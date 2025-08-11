import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heap.heappush(heap, -i)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            diff = a - b

            if diff != 0:
                heapq.heappush(heap, -diff)

        if len(heap) == 0:
            return 0
        else:
            return -heap[0]

