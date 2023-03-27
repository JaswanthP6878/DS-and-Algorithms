'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max1 = min(height[i], height[j])*(j-i)
        while i < j:
            value = min(height[i], height[j])*(j-i)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -=1
            else :
                i += 1
                j -= 1
            max1 = max(value, max1)
        
        return max1


'''
approach:
two pointers, one from first and other from last,
we decrease the pointer pointing to the smaller hieigh

'''