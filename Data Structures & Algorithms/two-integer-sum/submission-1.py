class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx in range(len(nums)):
            wanted = target - nums[idx]
            if wanted not in nums_dict:
                nums_dict[nums[idx]] = idx
            elif wanted in nums_dict:
                return [nums_dict[wanted], idx]

        #     if nums[idx] not in nums_dict:
        #         nums_dict[nums[idx]] = [idx]
        #     else:
        #         nums_dict[nums[idx]] += [idx]

        # for its, ids in nums_dict.items():
        #     wanted = target - nums_dict[its]
        #     if not any(wanted in values for values in nums_dict.values()):
        #         continue
            
