# Time:  O(n)
# Space: O(n)
# Leetcode # 58. Length of Last Word. @ Eric Liao April 18, 2017
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
# Runtime: 45 ms. Your runtime beats 54.73% of python submissions.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            return len(s.strip().split(' ')[-1])


if __name__ == "__main__":
    print Solution().lengthOfLastWord("Hello World")
    print Solution().lengthOfLastWord("")

