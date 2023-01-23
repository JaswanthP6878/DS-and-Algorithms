'''
242. Valid Anagram leetcode
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sv = [0]*26
        tv = [0]*26
        for i in s:
            sv[ord(i) - ord('a')] += 1
        for i in t:
            tv[ord(i) - ord('a')] += 1
        for i in range(26):
            if(sv[i] != tv[i]):
                return False
        return True
        
