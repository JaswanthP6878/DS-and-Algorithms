'''
125. Valid Palindrome
A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_f = ''
        for i in s:
            if( 0 <= ord(i) - ord('a')< 26 or 0<= ord(i) - ord('0') <= 9):
                s_f += i
        i = 0
        j = len(s_f) - 1
        print(s_f)
        while(i <= j):
            if(s_f[i] == s_f[j]):
                i += 1
                j -= 1
            else :
                return False
        return True
