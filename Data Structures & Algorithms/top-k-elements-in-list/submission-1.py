class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for num in nums:
            # dict.get(<key>, <default_value>)
            # Safe search the value for given key
            # return default_value is key not found
            countDict[num] = 1 + countDict.get(num, 0)
        
        freq_list = []
        for num, count in countDict.items():
            # Create a frequency list in the form:
            # [[frequency, value], ...] so that 
            # list.sort() sorts the list frequency-wise
            # in ascending order
            freq_list.append([count, num])
        freq_list.sort()

        # Return last k elements from sorted list
        return [num for count, num in freq_list[-k:]]