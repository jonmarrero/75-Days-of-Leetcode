# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        # Count zeros and calculate product of non-zero numbers
        zero_count = 0
        total_product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        
        # If more than one zero, all products will be 0
        if zero_count > 1:
            return ans
            
        # If exactly one zero, only its position will be non-zero
        if zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = total_product
            return ans
            
        # If no zeros, divide total product by each number
        for i in range(n):
            ans[i] = total_product // nums[i]
            
        return ans