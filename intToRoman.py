# Leetcode # 12. Integer to Roman. @ Eric Liao April 16, 2017
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = int(num)
        M = ["", "M", "MM", "MMM"]  # 1000-3000
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]  # 100-900
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]  # 10-90
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # 1-9
        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]

if __name__ == "__main__":
    print(Solution().intToRoman(999))
    print(Solution().intToRoman(3999))