class Solution:
    def compress(self, chars: List[str]) -> int:


        if len(chars) == 1:
            return 1

        l = 0
        count = 1
        for r in range(1, len(chars) + 1):
            if r < len(chars) and chars[l] == chars[r]:
                count += 1
   
            else:
                
                if count > 1:
                    for digit in str(count):
                        l += 1
                        chars[l] = digit

                l += 1

                if r < len(chars):
                    chars[l] = chars[r]

                count = 1

        return l
        