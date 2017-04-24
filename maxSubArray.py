# Time:  O(n)
# Space: O(1)
# Leetcode # 53. Maximum Subarray. @ Eric Liao April 19, 2017
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#

class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sublist_sum = []
        for i in range(len(nums)):
            n = i + 1
            while n <= len(nums):
                sublist_sum.append(sum(nums[i:n]))
                n += 1
        return max(sublist_sum)
    # this works but time-out when list become too large

    def maxSubArray2(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        maxSum = nums[0]
        minSum = 0
        sum = 0
        for num in nums:
            sum += num
            if sum - minSum > maxSum:
                maxSum = sum - minSum
            if sum < minSum:
                minSum = sum
        return maxSum
    # Runtime: 45 ms. Your runtime beats 98.77% of python submissions.


if __name__ == "__main__":
    print Solution().maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])
    print Solution().maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4])
