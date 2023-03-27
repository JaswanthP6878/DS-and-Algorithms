'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        d1 = dict()
        def util(n):
            if n==1:
                d1[1] = 1
                return d1[1]
            if n==2:
                d1[2] = 2
                return d1[2]
            if n in d1: return  d1[n]
            else:
                d1[n] = util(n-1) + util(n-2)
                return d1[n]
        util(n)
        return d1[n]

'''
approch memoize the values if they do not exist, we can create a dictonary so that we can 
and map them there, simlilar to the fibo nacci memoizatuion problem
'''
