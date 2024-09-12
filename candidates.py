class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        pas = 0
        out = 0

        while pas < k:
            possible = []
            if candidates * 2 >= len(costs):
                possible.extend(costs[:candidates])
                possible.extend(costs[:-candidates])

            else:
                possible = costs
            
            cheapest = float('inf')
           
            for i in possible:
                if i < cheapest:
                    cheapest = i
            out += cheapest
            costs.remove(cheapest)
            pas += 1
        return out
