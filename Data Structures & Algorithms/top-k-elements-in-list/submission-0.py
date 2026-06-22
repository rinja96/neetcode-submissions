class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)
        
        freq_list = []
        for num, count in countDict.items():
            freq_list.append([count, num])
        freq_list.sort()

        return [num for count, num in freq_list[-k:]]