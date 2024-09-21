class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        d = {}

        for i in grid:
            e = ', '.join(str(x) for x in i)
            
            if e in d:
                d[e] += 1
            else:
                d[e] = 1

        out = 0
        for i in range(len(grid[0])):
            col = [row[i] for row in grid]

            e = ', '.join(str(x) for x in col)

            if e in d:
                out += d[e]


        return out