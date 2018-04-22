import heapq
from heapq import heappush, heappop

class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        not_flippable = set()
        heap = []

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                not_flippable.add(fronts[i])
                if fronts[i] in heap:
                    heap = [val for val in heap if val != fronts[i]]
                    heapq.heapify(heap)
            else:
                if fronts[i] not in not_flippable:
                    heappush(heap, fronts[i])
                if backs[i] not in not_flippable:
                    heappush(heap, backs[i])
        ans =  heap[0] if len(heap) > 0 and heap[0] not in not_flippable else 0
        return ans
