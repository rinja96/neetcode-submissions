class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Trick:
            As we iterate over the list:
            - Find difference with current element.  
            - Search the new nums_dict for this difference.
            - If not found, we add current element to the dict.
            - Ultimately we will find the 2nd number in the list.
            - Its difference will already be present in the dict.
        """
        nums_dict = {}
        for idx in range(len(nums)):
            # 1. What is the required number?
            wanted = target - nums[idx]
            # 2. Add number if it is not in our dynamic dict
            if wanted not in nums_dict:
                nums_dict[nums[idx]] = idx
            # 3. We are looking back to get the smaller idx
            elif wanted in nums_dict:
                return [nums_dict[wanted], idx]
