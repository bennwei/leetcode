# Leetcode # 28. Implement strStr(). @ Eric Liao April 18, 2017
# Implement strStr().
#
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
# Time:  O(n + k)
# Space: O(k)
# Runtime: 45 ms, Your runtime beats 75.54% of python submissions.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

    def strStr2(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """
            try:
                return haystack.index(needle)
            except:
                return -1




if __name__ == "__main__":
    print Solution().strStr("abcd", "d")
    print Solution().strStr("abababcdab", "ababcdx")
