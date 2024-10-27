class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        results = [-1] * len(nums)
        i = 0
        length = len(nums)
        while i < length * 2:
            n = nums[i%length]
            if not stack or n <= nums[stack[-1]]:
                stack.append(i%length)
                i +=1
            else:
                idx = stack.pop()
                results[idx] = n

        return results
    