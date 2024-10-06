class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        d = {}
        output = 0
        for i in nums:
            complement = k - i
            if complement in d:
                if d[complement] > 0:
                    output += 1
                    d[complement] -= 1
                else:
                    if i in d:
                        d[i] += 1
                    else:
                        d[i] =1
            else:
                if i in d:
                        d[i] += 1
                else:
                    d[i] =1

        return output
            