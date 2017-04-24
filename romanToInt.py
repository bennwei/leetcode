# Leetcode # 13. Roman to Integer. @ Eric Liao April 16, 2017
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Time:  O(n)
# Space: O(1)


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                res += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                res += roman[s[i]]
        return res

if __name__ == "__main__":
    print (Solution().romanToInt("V"))
    print (Solution().romanToInt("MMMCMXCIX"))
