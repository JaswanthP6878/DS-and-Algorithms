'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        nums = []
        operands = ['+', '-', '*', '/']
        for i in tokens:
            if(i not in operands):
                nums.append((i))
            else :
                a = int(nums.pop())
                b = int(nums.pop())
                if i == '+':
                    nums.append(int(a + b))
                if i == '-':
                    nums.append(int(b-a))
                if i == '*':
                    nums.append(int(a*b))
                if i == '/':
                    nums.append(int(b/a))
                # print(nums[-1])
        return nums[0]
