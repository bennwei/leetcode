# Leetcode # 9. Palindrome Number. @ Eric Liao 2017
# Determine whether an integer is a palindrome. Do this without extra space.
# Runtime: 205 ms， Your runtime beats 95.48% of python submissions.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]