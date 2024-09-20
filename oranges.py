class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        q = deque([])

        freshC = 0
        time = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshC += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        while q and freshC > 0:
            print(q)
            time += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for rd, rc in directions:
                    nr = r + rd
                    nc = c + rc
    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1 and (nr, nc) not in visited:
                            freshC -= 1
                            q.append((nr, nc))
                            visited.add((nr, nc))
                            grid[nr][nc] == 2
                            
        
        if freshC > 0:
            return -1
        else:
            return time
