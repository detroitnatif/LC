class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[float('inf') for i in range(len(word2)+1)] for j in range(len(word1) + 1)]
        r, c = len(word2), len(word1)
        for i in range(r + 1):
            dp[c][i] = r - i

        for j in range(c + 1):
            dp[j][r] = c - j

        
        for ci in range(c - 1, -1, -1):
            for ri in range(r - 1, -1, -1):
                if word1[ci] == word2[ri]:
                    dp[ci][ri] = dp[ci+1][ri+1]
                else:
                    dp[ci][ri] = 1 + min(dp[ci + 1][ri], dp[ci][ri+1], dp[ci+1][ri+1])
        return dp[0][0]