class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1000000007
        memo = {}

        def dp(i):
            if i == 0:
                return 1  # An empty board has exactly one way to tile it (by doing nothing).
            if i == 1:
                return 1  # A 2 x 1 board can only be covered by one vertical domino.
            if i == 2:
                return 2  # A 2 x 2 board can be tiled with two vertical or two horizontal dominoes.
            if i in memo:
                return memo[i]

            # Recursive transitions
            # dp(i - 1): place one vertical domino
            # dp(i - 2): place two horizontal dominoes
            # 2 * dp(i - 3): place one tromino and account for its two possible placements
            memo[i] = (dp(i - 1) + dp(i - 2) + 2 * dp(i - 3)) % mod
            return memo[i]

        return dp(n)
        