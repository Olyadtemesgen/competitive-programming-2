class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        m = len(nums)
        for i in range(m+1):
            if i not in nums:
                return i