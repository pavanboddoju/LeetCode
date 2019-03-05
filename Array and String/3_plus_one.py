class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        
        for n in digits:
            num += str(n)
        
        return [int(x) for x in str(int(num)+1)]