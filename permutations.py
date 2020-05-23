class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        permutations = []
        self.permutations_helper(nums, [], permutations)
        return permutations

    
    def permutations_helper(self, nums, permutation, permutations):
        if not nums:
            permutations.append(permutation)
            return

        for i in range(len(nums)):
            self.permutations_helper(nums[:i] + nums[i + 1:], permutation + [nums[i]], permutations)
        return
