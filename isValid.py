# Leetcode # 12. Valid Parentheses. @ Eric Liao April 16, 2017
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
# Runtime: 65 ms. Your runtime beats 21.08% of python submissions.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Return True if all delimiters are properly match; False otherwise.
        """
        left = '({['  # opening delimiters
        right = ')}]'  # respective closing delims

        S = []  # use list as LIFO stack
        for c in s:
            if c in left:
                S.append(c)  # push left delimiter on stack
            elif c in right:
                if len(S) == 0:
                    return False  # nothing to match with
                if right.index(c) != left.index(S.pop()):
                    return False  # mismatched
        return len(S) == 0  # Stack is empty if all symbols matched


if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")