class Solution:
    def climbStairs(self, n: int) -> int:
        store = [1, 2]
        if n == 0 or n == 1:
            return 1
        else:
            i = 2
            for i in range(2, n):
                store[0], store[1] = store[1], store[0]
                store[1] = store[0] + store[1]
            return store[1]