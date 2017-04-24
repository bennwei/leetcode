# Leetcode # 7. Reverse Integer. @ Eric Liao 2017
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# Runtime: 49 ms, Your runtime beats 96.13% of python submissions.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x == 0:
        # res = int(0)
        if x % 10 == 0:
            res = x / 10 * len(str(x))

        if x >= 0:
            res = int(str(x)[::-1])

        if x < 0:
            res = int('-' + str(abs(x))[::-1])

        if res > 2147483647 or res < -2147483648:
            res = 0

        return res

# Test case
x1 = 123
x2 = -123
x3 = 0
x4 = -90000

if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-321))
