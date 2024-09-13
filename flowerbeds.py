class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n == 0:
                return True

        for i in range(1, len(flowerbed) - 1):
            print(i)
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:

                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

                else:
                    pass

        if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n != 0:
            n -= 1

        
        return n == 0

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = False
        right = False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:

                if i == 0 or flowerbed[i - 1] == 0:
                    left = True
                
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    right = True
                
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True

                left = False
                right = False

        return n == 0
        