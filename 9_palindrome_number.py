class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # check if x is less than 0, if it's return false
        # initialize a new variable r with the value of x
        # initialize a new variable y with a value of x%10
        # modify x by the value of x/10
        # use loop until x/10 becomes 0
        # inside of the loop modify the value of y by y*10+(x%10)
        # then modify x by the value of x/10
        # after the loop ends check if x and y equal
        #     if they aren't return false otherwise return true

        if x < 0:
            return False
        
        r = x
        y = x % 10
        x = x // 10

        while ((x % 10) != 0 or x//10 != 0):
            y = (y * 10) + (x % 10)
            x = x // 10

        if r != y:
            return False
        return True

        
        

# x = 121
x = -121
# x = 10
# x = 1001
sol = Solution()
res = sol.isPalindrome(x)
print(res)