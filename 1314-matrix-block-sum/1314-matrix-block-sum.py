class Solution(object):
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        # Step 1: Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = (
                    mat[i][j]
                    + prefix[i][j+1]
                    + prefix[i+1][j]
                    - prefix[i][j]
                )

        # Step 2: Compute result
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)

                # shift by +1 because prefix is 1-indexed
                r1 += 1
                c1 += 1
                r2 += 1
                c2 += 1

                result[i][j] = (
                    prefix[r2][c2]
                    - prefix[r1-1][c2]
                    - prefix[r2][c1-1]
                    + prefix[r1-1][c1-1]
                )

        return result