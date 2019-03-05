class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if (length <= 2):
            return -1
        left = 0
        right = sum(nums)
        for n in range(length):
            right -= nums[n]
            if (left == right):
                return n
            left += nums[n]
        return -1

        