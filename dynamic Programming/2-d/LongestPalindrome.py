'''
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*(n+1) for _ in range(n+1)]
        
        for i in range(n): dp[i][i] = True #single len strings are palindromes
        ans = [0,0]
        #finding length 2 palindromes:
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]
        
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                if (s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    ans = [i,j]
        
        i,j = ans
        return s[i: j+1]


                

        




