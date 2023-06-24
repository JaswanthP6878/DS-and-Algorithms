'''
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            lcs[i:j] => longest subsequence for text1[i:] and text2[j:]
            lcs[i:j] = 
                        if i ==j lcs[i+1,j+1]],
                        else max(lcs[i, j+1] or lcs[i+1, j])
                        )

            lcs[n:m] if n == m : 
        '''
        n = len(text1); m = len(text2);
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]