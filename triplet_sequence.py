class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        f, m, l = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] < nums[f]:
                print("first")
                f = i
                m = i
                l = i
            elif nums[i] > nums[f]:
                print('middle')
                if nums[i] > nums[m]:
                    m = i
                if nums[i] > nums[l]:
                    l = i
            elif nums[i] > nums[m]:
                print('last')
                l = i


        if f < m and m < l:
            return True
        else:
            return False
        
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')

        for i in nums:

            if i <= first:
                first = i
            elif i <= second:
                second = i

            else:
                return True

        return False
    

# SOLVED
