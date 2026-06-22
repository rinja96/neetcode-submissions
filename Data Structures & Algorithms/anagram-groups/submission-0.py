from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary that stores lists by default:
        # A dictionary with a machine attached 
        # that automatically creates an empty list 
        # when a new key appears.
        result = defaultdict(list)

        for s in strs:
            # Go through all the strings in strs
            
            # Create a new string of sorted characters
            sortedS = ''.join(sorted(s))
            # With the sorted string as key,
            # append OG string in value list
            result[sortedS].append(s)
            # result might look like:
            # {
            #   "act" : ["act", "cat"],
            #   "opst": ["pots", "tops", "stop"],
            #   "aht" : ["hat"]
            # }
        return list(result.values())
