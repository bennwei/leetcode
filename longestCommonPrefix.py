# Leetcode # 12. Integer to Roman. @ Eric Liao April 16, 2017
# Write a function to find the longest common prefix string amongst an array of strings.
# Runtime: 69 ms. Your runtime beats 18.38% of python submissions.

import os

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["hello", "heaven", "heavy"])