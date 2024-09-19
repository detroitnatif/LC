class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        st = ""
        k = 0

        for i in s:
            if i.isdigit():
                k = k * 10 + int(i)
            elif i == "[":
                stack.append((k, st))
                st = ""
                k = 0
            elif i == "]":
                prevN, prevS = stack.pop()
                st = prevS + prevN * st 

            else:
                st += i

        return st