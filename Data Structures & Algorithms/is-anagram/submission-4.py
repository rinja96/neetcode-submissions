class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s_dict = {}
        # for char_idx in range(len(s)):
        #     if s[char_idx] not in s_dict:
        #         s_dict[s[char_idx]] = 1
        #     if s[char_idx] in s_dict:
        #         s_dict[s[char_idx]] += 1

        # t_dict = {}
        # for char_idx in range(len(t)):
        #     if t[char_idx] not in s_dict:
        #         return False
        #     if t[char_idx] not in t_dict:
        #         t_dict[t[char_idx]] = 1
        #     if t[char_idx] in t_dict:
        #         t_dict[t[char_idx]] += 1

        # for char, count in t_dict.items():
        #     if count != s_dict[char]:
        #         return False

        # return True
        h_set = {}
        for i in range(len(s)):
            h_set[s[i]] = h_set.get(s[i], 0) + 1
            h_set[t[i]] = h_set.get(t[i], 0) - 1

        return all(v == 0 for v in h_set.values())

