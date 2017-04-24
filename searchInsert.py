# Leetcode # 35. Search Insert Position. @ Eric Liao April 18, 2017
# Given a sorted array and a target value, return the index if the target is found.
#
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
# Runtime: 38 ms. Your runtime beats 96.90% of python submissions.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        else:
            for i in range(0, len(nums) - 1):
                if target > nums[i] and target < nums[i + 1]:
                    return i + 1

if __name__ == "__main__":
    print Solution().searchInsert([1, 3, 5, 6], 5)
    print Solution().searchInsert([1, 3, 5, 6], 2)
    print Solution().searchInsert([1, 3, 5, 6], 7)
    print Solution().searchInsert([1, 3, 5, 6], 0)