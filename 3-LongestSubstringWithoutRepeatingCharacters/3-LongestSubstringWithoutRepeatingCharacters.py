class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_set = set()
        #two pointer method
        left = 0
        max_length = 0 

        # iterate with the right pointer
        for right in range(len(s)):
            # if the character at the right pointer is already in the set
            while s[right] in char_set:
                # remove the character at the left pointer from the set
                char_set.remove(s[left])
                # move the left pointer to the right
                left += 1
            # add the character at the right pointer to the set
            char_set.add(s[right])
            # update the maximum length if the current window is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length


# Time complexity: O(n), where n is the length of the string
# Space complexity: O(min(n, m)), where n is the length of the string and m is the character set size
        
