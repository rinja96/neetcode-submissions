class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h_set = {}
        for i in range(len(s)):
            # dict.get(key, default_value)
            # Safe search key's value in dict
            # If present, returns value
            # If not present, returns defined default_value
            h_set[s[i]] = h_set.get(s[i], 0) + 1
            h_set[t[i]] = h_set.get(t[i], 0) - 1

        # all([...]) returns True only if all elements are True
        # E.g.,
        # all([True, True, False]) returns False
        # all([True, True, True]) returns True
        return all(v == 0 for v in h_set.values())

