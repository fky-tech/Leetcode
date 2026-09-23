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
        return None

# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6

nums = [3,3]
target = 6

s = Solution()
output = s.twoSum(nums, target)
print(output)
