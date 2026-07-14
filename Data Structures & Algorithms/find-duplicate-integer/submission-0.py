class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hasset = set()

        for i in nums:
            if i in hasset:
                return i
            else:
                hasset.add(i)
        return False