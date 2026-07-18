class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)

        prod = 1
        for idx in range(1, len(nums)):
            prod *= nums[idx - 1]
            prefix[idx] = prod

        prod = 1
        for idx in range(len(nums) - 2, -1, -1):
            prod *= nums[idx + 1]
            suffix[idx] = prod

        for idx in range(len(nums)):
            output[idx] = suffix[idx] * prefix[idx] 

        return output
