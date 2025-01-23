# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109




class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = 1

        """
        n^2 is 1,000,000,000 so no n^2

        brute force would take too long
        
        this is a variant of two sum.
        if we store the two sum, we know what indices we can immediately remove
        """
        h = defaultdict(list)
        for ni, n in enumerate(nums):
            h[n].append(ni)

        
        if len(h) == 1:  # edge case: all same number, like k=10, [5,5,5,5.........5,5]
            if list(h.keys())[0] == k / 2:
                return len(nums) // 2
            return 0

        used = set()  # no need to actually remove elements which would mess up all the indices in h
        ops = 0
        i = 0
        while nums and i < len(nums):
            if i in used:
                i += 1
                continue

            target = k - nums[i]
            if h.get(target) != []:
                for ind_i, ind in enumerate(h[target]):
                    if ind > i and ind not in used:
                        ops += 1
                        used.add(i)
                        used.add(ind)
                        break
            
            i += 1
        
        return ops