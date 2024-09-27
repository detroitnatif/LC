class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        out = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == '1':
    
                    q.append((i, j))
                    visited.add((i, j))
                    islands += 1
                while q:
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == '1':
                            q.append((nr, nc))
                            visited.add((nr, nc))
        return islands
