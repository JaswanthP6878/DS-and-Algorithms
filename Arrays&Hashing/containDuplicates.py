'''
217. Contains Duplicate leetcode
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        k  = len(nums)
        for i in range(k-1):
            if(nums[i] == nums[i+1]):
                return True
        return False
