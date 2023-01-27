'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = dict()

        for w in strs:
            key = ''.join(sorted(w))
            if key not in sol:
                sol[key] = [w]
            else :
                sol[key].append(w)
        return [w for w in sol.values()]