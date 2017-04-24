# Leetcode # 26. Remove Duplicates from Sorted Array. @ Eric Liao April 17, 2017

#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
# Runtime: 79 ms. Your runtime beats 95.57% of python submissions.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return len(set(nums))

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1


if __name__ == "__main__":
    print Solution().removeDuplicates([1,1,2])
    print Solution().removeDuplicates2([1, 1, 2])