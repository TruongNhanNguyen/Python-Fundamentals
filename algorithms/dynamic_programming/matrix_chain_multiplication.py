import unittest
from typing import List, Tuple


def matrix_chain_multiplication(matrices: List[Tuple[int, int]]) -> int:
    n = len(matrices)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n - 1]


class TestMatrixChainMultiplication(unittest.TestCase):
    def test_matrix_chain_multiplication(self):
        self.assertEqual(matrix_chain_multiplication([(10, 30), (30, 5), (5, 60)]), 3000)
        self.assertEqual(matrix_chain_multiplication([(40, 20), (20, 30), (30, 10), (10, 30)]), 24000)
        self.assertEqual(matrix_chain_multiplication([(5, 4), (4, 6), (6, 2), (2, 18)]), 240)
        self.assertEqual(matrix_chain_multiplication([(5, 4), (4, 6), (6, 2), (2, 18), (18, 3)]), 414)


if __name__ == '__main__':
    unittest.main()
