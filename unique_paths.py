class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bot = [1] * n

        for i in range(m - 2, -1, -1):
            
            for j in range(n - 2, -1, -1):
                bot[j] += bot[j+1]
            
        return bot[0]
    
    