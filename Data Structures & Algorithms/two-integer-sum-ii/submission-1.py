class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_1 = 0
        ptr_2 = len(numbers) - 1

        while ptr_1 < ptr_2:
            search = target - numbers[ptr_1]
            if search > numbers[ptr_2]:
                ptr_1 += 1
            elif search < numbers[ptr_2]:
                ptr_2 -= 1
            else:
                return [ptr_1 + 1, ptr_2 + 1]
