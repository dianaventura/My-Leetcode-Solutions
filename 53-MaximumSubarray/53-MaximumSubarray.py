class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #keeping track of current and best
        current = 0 
        best = nums[0]
        #for every number add it to current and if it is higher than the current best update best
        #if current is less than zero then set current to 0 
        for num in nums: 
            current += num

            if current > best: 
                best = current
            if current < 0:
                current = 0
        return best

        #time complexity O(n) because the loop runs once for each element in the input array
        #space complexity O(1) because we have two fixed variables 

