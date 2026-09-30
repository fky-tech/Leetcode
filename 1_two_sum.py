#O(n^2) solution
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
'''

#O(nlogn) solution if nums value is sorted
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Sort nums
        # Iterate through nums from index 0 to length of nums
        # Store first and last index of nums into sm and lg respectively
        # Store the sum of sm and lg index values to sum
        # If sum is equal to target, return sm and lg
        # Else sum is less than the target, increment sm
        # Else sum is greater than the target, decrement lg
        # If the loop ends without returning, return none

        # nums.sort()

        sm = 0
        lg = len(nums)-1

        for i in range(0, len(nums)-1):
            sum = nums[sm] + nums[lg]
            if sum == target:
                return [sm, lg]
            elif sum < target:
                sm += 1
            elif sum > target:
                lg -= 1
        return []
'''

#O(n) solution if nums not sorted(nums used as it is without sorting it)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Initialize hashTable with empty dictionary
        # Iterate through nums and store the nums value as key and its index as value in the hash table
        # Iterate through nums and check if target - current index of nums value gets inside of the hashTable
        # If found, check if current index is not equals to that hashTable value, if it equals skip to the
            # next iteration, if it's not equal return the current index and the hashTable value

        hashTable = {}

        for i in range(len(nums)):
            hashTable[nums[i]] = i

        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashTable and hashTable[val]!=i:
                return [i, hashTable[val]]

        return []


# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

# nums = [3,3]
# target = 6

s = Solution()
output = s.twoSum(nums, target)
print(output)
