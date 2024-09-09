class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_most = 0
        left_sum = 0
        right_sum = 0

        for i in range(len(nums)):
            left_sum = sum(nums[:i+1])
           
            right_sum = sum(nums[i:])
            
            if left_sum == right_sum:
                return i

        return -1