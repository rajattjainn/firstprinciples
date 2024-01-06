# Leet Code Problem # 283: https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zeroes = []
        for i in range(len(nums)):
                if nums[i] != 0:
                        non_zeroes.append(i)

        for i in range(len(non_zeroes)):
                nums[i] = nums[non_zeroes[i]]
        
        for i in range (len(non_zeroes), len((nums))):
                nums[i] = 0
        return nums

nums = [0]
print (moveZeroes(nums))
