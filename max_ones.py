

def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        for i, e in enumerate(nums):
            lives = k
            count = 0
            pos = i
        
            while lives >= 0 and pos < len(nums):
                if nums[pos] == 0:
                    lives -= 1
                if lives >= 0:
                    count += 1
                pos += 1
            longest = max(longest, count)
        
        return longest