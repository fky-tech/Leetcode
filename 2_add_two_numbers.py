class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Check which list is greater in length and store the highest one in variable s
        # Initialize 3 hash tables h1, h2, and r with empty list
        # loop through l1, l2 and store l1 and l2 list indices as key and list values as value in h1 and h2
        # while looping in l1 and l2, if one of them length is lower than s, append 0 to match its len as s
        # start a loop from 0 to s
        # then check if current index sum of h1 and h2 equals to 10
        # if it's equal, store 0 to the current index of r and add 1 to next index value of h1
        # if it's greater than 10, first check if it's equals to 11
        #     if it's store 1 to the current index of r and add 1 to the next index value of h1
        #     if it's greater than 11, divide the modules of h1 current index with 10, then
        #     store the modules value in r current index and add 1 to the next index value of h1
        # if it's less than 10, store the sum of h1 and h2 to current index of r

        if len(l1) > len(l2):
            s = len(l1)
        else:
            s = len(l2)

        h1 = {}
        h2 = {}
        r = {}

        for i in range(0, s):
            if i >= len(l1):
                h1[i] = 0
            else:
                h1[i] = l1[i]

            if i >= len(l2):
                h2[i] = 0
            else:
                h2[i] = l2[i]

        for i in range(0, s):
            if (h1[i] + h2[i] == 10):
                r[i] = 0
                if (i != s-1):
                    h1[i+1] += 1
                else:
                    r[i+1] = 1
            elif (h1[i] + h2[i] > 10):
                if (h1[i] + h2[i] == 11):
                    r[i] = 1
                    if (i != s-1):
                        h1[i+1] += 1
                    else:
                        r[i+1] = 1
                else:
                    r[i] = (h1[i] + h2[i]) % 10
                    if (i != s-1):
                        h1[i+1] += 1
                    else:
                        r[i+1] = 1
            else:
                r[i] = h1[i] + h2[i]

        return list(r.values())

# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# l1 = [0]
# l2 = [0]
sol = Solution()
res = sol.addTwoNumbers(l1, l2)
print(res)