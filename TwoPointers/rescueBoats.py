'''
881. Boats to Save People
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        boats = 0
        people.sort()
        l = 0
        r = n - 1 
        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else :
                boats += 1
                r -= 1
        # if l == r : boats += 1
        return boats

'''
approach: 
sort the members on the boat, have a left and right pointer for first and last person, add them
and check with limit

is sum <= limit: add both of them to a boat, increase boat count by 
if sum > limit: decrease the fat guy/ right pointer and add him to a boat


continue till l <= r 


'''

