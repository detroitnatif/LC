class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        maxO = 0
        l = 0
        flip = False
        for r in range(len(nums)):
            if nums[r] == 0 and not flip:
                flip = True

            elif nums[r] == 0 and flip:
                while nums[l] != 0:
                    l += 1
                l += 1

            amt = r - l
            maxO = max(amt, maxO)
        
        return maxO