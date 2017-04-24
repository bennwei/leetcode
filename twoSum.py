# Leetcode # 1. Two Sum. @ Eric Liao April 2017
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# Runtime: 49 ms, Your runtime beats 96.13% of python submissions.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return -1
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i, nums[i+1:].index(diff) + i + 1]

if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))
