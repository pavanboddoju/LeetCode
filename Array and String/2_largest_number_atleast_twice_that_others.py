class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        first = -1
        second = -1
        index = 0
        
        for n in range(length):
            current = nums[n]
            if first < current:
                second = first
                first = current
                index = n
            elif second < current:
                second = current
        
        if first >= second*2:
            return index
        return -1
        
        