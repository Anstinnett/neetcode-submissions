class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negativenums = [-x for x in nums]
        heapq.heapify(negativenums)

        while k >1:
            heapq.heappop(negativenums)
            k-=1
        res = heapq.heappop(negativenums)
        res = res *-1
        return res 
        