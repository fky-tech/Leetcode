class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialize a new variable x with value 0
        # use hash table and store the characters with their value
        # use a loop to go from size of s to 0 and check if the current index is "V" or "X" 
            # then check if the next is "I", if it's "I" subtract from V or X from I and the same for L, C and D, M.
        # add the value of the current chars value to x, then after the loop ends return x.

        x = 0
        h = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }


        i = len(s) -1
        while(i > -1):
            if s[i] == "V":
                if s[i-1] == "I" and i!=0:
                    x += (h["V"] - h["I"])
                    i -= 1
                else:
                    x += h["V"]
            elif s[i] == "X":
                if s[i-1] == "I" and i!=0:
                    x += (h["X"] - h["I"])
                    i -= 1
                else:
                    x += h["X"]
            elif s[i] == "L":
                if s[i-1] == "X" and i!=0:
                    x += (h["L"] - h["X"])
                    i -= 1
                else:
                    x += h["L"]
            elif s[i] == "C":
                if s[i-1] == "X" and i!=0:
                    x += (h["C"] - h["X"])
                    i -= 1
                else:
                    x += h["C"]
            elif s[i] == "D":
                if s[i-1] == "C" and i!=0:
                    x += (h["D"] - h["C"])
                    i -= 1
                else:
                    x += h["D"]
            elif s[i] == "M":
                if s[i-1] == "C" and i!=0:
                    x += (h["M"] - h["C"])
                    i -= 1
                else:
                    x += h["M"]
            else:
                x += h["I"]
            i-=1
        return x

# s = "III"
# s = "LVIII"
# s = "MCMXCIV"
# s ="MCDLXXVI"
s = "MMMCDXC"
sol = Solution()
res = sol.romanToInt(s)
print(res)
