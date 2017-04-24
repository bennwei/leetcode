# Leetcode # 27. Remove Element. @ Eric Liao April 17, 2017
#
# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Time:  O(n)
# Space: O(1)
# Runtime: 42 ms. Your runtime beats 88.74% of python submissions.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        le = len(nums)
        count = 0
        for i in range(0, le):
           if nums[i] != val:
               nums[count] = nums[i]
               count += 1
        return count

if __name__ == "__main__":
    print Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2)