class Solution:
    def climbStairs(self, n: int) -> int:
        
        def multiply(A, B):
            return [
                [
                    A[0][0] * B[0][0] + A[0][1] * B[1][0],
                    A[0][0] * B[0][1] + A[0][1] * B[1][1],
                ],
                [
                    A[1][0] * B[0][0] + A[1][1] * B[1][0],
                    A[1][0] * B[0][1] + A[1][1] * B[1][1],
                ],
            ]
        
        def matrix_power(M, power):
            result = [
                [1, 0], 
                [0, 1],
            ]

            base = M

            while power > 0: 
                if power % 2 == 1:
                    result = multiply (result, base)

                base = multiply(base, base)
                power //= 2

            return result

        def calculate_fib(n):
            if n == 0:
                return 0

            M = [
                [1, 1],
                [1, 0],
            ]

            powered = matrix_power(M, n)

            return powered[0][1]

        return calculate_fib(n + 1)
