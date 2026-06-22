class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countValues = {}
        for num in nums:
            if num not in countValues:
                countValues[num] = 1
            else:
                return True
        return False