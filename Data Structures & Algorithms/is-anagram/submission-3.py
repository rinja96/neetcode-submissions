class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for char_idx in range(len(s)):
            if s[char_idx] not in s_dict:
                s_dict[s[char_idx]] = 1
            if s[char_idx] in s_dict:
                s_dict[s[char_idx]] += 1

        t_dict = {}
        for char_idx in range(len(t)):
            if t[char_idx] not in s_dict:
                return False
            if t[char_idx] not in t_dict:
                t_dict[t[char_idx]] = 1
            if t[char_idx] in t_dict:
                t_dict[t[char_idx]] += 1

        for char, count in t_dict.items():
            if count != s_dict[char]:
                return False

        return True


