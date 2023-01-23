'''
20. Valid Parentheses leetcode
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        for i in s:
            if i in opens:
                stack.append(i)
            if i == ']' :
                if len(stack) == 0:
                    return False
                elif(stack[-1] == '['):
                    stack.pop()
                else :
                    return False
            if i == ')' :
                if len(stack) == 0:
                    return False
                elif(stack[-1] == '('):
                    stack.pop()
                else :
                    return False
            if i == '}' :
                if len(stack) == 0:
                    return False
                elif(stack[-1] == '{'):
                    stack.pop()
                else :
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False