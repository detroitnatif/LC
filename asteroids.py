class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        out = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            if a < 0:
                if not stack:
                    out.append(a)
                while stack:
                    if (abs(a)) > stack[-1]:
                        stack.pop()

                    elif abs(a) == stack[-1]:
                        stack.pop()
                        break

                    else:
                        break

                    if len(stack) == 0:
                        out.append(a)

        
        return out + stack

