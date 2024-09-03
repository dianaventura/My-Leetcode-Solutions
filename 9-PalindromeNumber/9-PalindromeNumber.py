class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # A negative number can't be a palindrome
        # Also, any number that ends with 0 cannot be a palindrome, except 0 itself
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Revert half of the number to check for palindrome
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # If the number is odd, discard the middle digit
        return x == reversed_half or x == reversed_half // 10
