# Leetcode # 557. Reverse Words in a String III. @ Eric Liao April 17, 2017
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
# Runtime: 45 ms


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([c[::-1] for c in s.split(' ')])


if __name__ == "__main__":
    print Solution().reverseWords("Let's take LeetCode contest")