'''
213. House Robber II
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def hhelper1(self, nums):
        n = len(nums)
        dp = [0]*(n+2)
        for i in reversed(range(n)):
            dp[i] = max(nums[i]+ dp[i+2],dp[i+1])
        return dp[0]
    
    def rob(self, nums: List[int]) -> int:
        '''
        reuse house robber 1 function, but take two possibilities from the given array
        first is without the first element , and next is without the last element so, we get
        two cases. len(num) == 1 is an edge case.
        '''
        if len(nums) == 1 : return nums[0]
        return max(self.hhelper1(nums[:-1]), self.hhelper1(nums[1:]))
