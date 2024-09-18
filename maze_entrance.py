class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cols = len(maze[0])
        rows = len(maze)

        q = deque([entrance])
        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = 0
        
        while q:
            count += 1
            for que in range(len(q)):
                r,c = q.popleft()
                for rd, cd in directions:
                    nr = r + rd
                    nc = c + cd

                    if 0 <= nr < rows and 0 <= nc < cols and (((nr, nc)) not in visited) and maze[nr][nc] == '.':
                        
                        if (nr == rows - 1 or nc == cols -1 or nc == 0 or nr == 0) and (nr, nc) != (entrance[0], entrance[1]) and maze[nr][nc] == '.':
                              
                            return count
                        else:
                            q.append([nr, nc])
                            visited.add((r,c))
                            

        return -1
    
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cols = len(maze[0])
        rows = len(maze)

        q = deque([entrance])
        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        count = 0

        while q:
            count += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))
                for rd, cd in directions:
                    nr = r + rd
                    nc = c + cd
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] == '.':
                        if (nr == rows - 1 or nr == 0 or nc == cols - 1 or nc == 0) and (nr, nc) != (entrance[0], entrance[1]):
                            return count
                    q.append([nr, nc])
                    visited.add((nr, nc))

        return -1