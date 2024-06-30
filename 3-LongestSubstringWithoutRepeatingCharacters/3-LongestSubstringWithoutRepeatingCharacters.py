            while s[right] in char_set:
                # remove the character at the left pointer from the set
                char_set.remove(s[left])
                # move the left pointer to the right
                left += 1
            # add the character at the right pointer to the set
            char_set.add(s[right])
            # update the maximum length if the current window is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length


# Time complexity: O(n), where n is the length of the string
# Space complexity: O(min(n, m)), where n is the length of the string and m is the character set size
        
"
