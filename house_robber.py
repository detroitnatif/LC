class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)

        for i in range(len(nums) - 3, -1, -1):

            if nums[i] + nums[i+2] >= nums[i+1]:
                nums[i] += nums[i+2]

            else:
                nums[i] = nums[i+1]
    
        return max(nums[0], nums[1])