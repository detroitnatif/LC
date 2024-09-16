class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n

        left = 0
        for i in range(1, n):
            
            if temperatures[left] < temperatures[i]:
                output[left] = i - left
                left = i

            else:
                temp = i
                while temp < n and temperatures[temp] <= temperatures[left]:
                   temp += 1
     
                if temp < n:
                    output[left] = temp - left

                else:
                    output[left] = 0

                left = i

        return output
        