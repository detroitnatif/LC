class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        Rq = deque()
        Dq = deque()
        l = len(senate)

        for i, e in enumerate(senate):
            if e == "D":
                Dq.append(i)
            elif e == "R":
                Rq.append(i)


        while Rq and Dq:

            r = Rq.popleft()
            d = Dq.popleft()

            if r < d:
                Rq.append(r + l)
            else:
                Dq.append(d + l)

        
        if len(Rq) == 0:
            return "Dire"

        else:
            return "Radiant"
            