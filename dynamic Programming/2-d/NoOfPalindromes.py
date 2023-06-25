'''
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
            In this approach we are using dp,
            with dp[i][j] representing True if s[i][j] is a substring
            then we add all the cases. 
        '''

        n = len(s)
        dp = [[False]*n for _ in range(n)]

        ans = 0
        for i in range(n): 
            dp[i][i] = 1; ans += 1
 
        #for len 2 substrings
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1

        for diff in range(2,n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    ans += 1
                    dp[i][j] = True    
        
        return ans
    
    # approach  2
    def ManachersAlgo(self, s: str) -> int:
        '''
        Manachers algorithm involves finding number of palidromes centering around 
        each element of a string. 

        Two cases 
        1) odd palindromes centering around every element -> we take left and right 
        pointer and expand them to left and right 

        2) even palindromes: consider two elements at a time and expand them
        
        '''

        res = 0
        for i in range(len(s)):
            # for odd palindroms
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res



    
