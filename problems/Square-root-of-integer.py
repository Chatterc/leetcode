# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
#
# Example 1:
# Input: x = 4
# Output: 2
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
# Constraints:
# 0 <= x <= 231 - 1

class Solution:
    """
    Quick and easiest way to calculate the sqare root of an integer with O(1) complexity
    Note: decimals will be truncated
    """
    def mySqrt(self, x: int) -> int:
        x = int(x**0.5)
        return x
    

def main():
    ans = Solution().mySqrt(x=4)
    print(ans) # expected 2
    
    ans = Solution().mySqrt(x=8)
    print(ans) # expected 2
    

if __name__ == '__main__':
    main()