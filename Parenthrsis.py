# Given a balanced parentheses string s, return True if it is valid and False if it is invalid.
# A valid string has the following properties:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

from gettext import find
from pip import main


class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Case 1: if len(s) is not even
        # Case 2: () is valid
        if len(s) % 2 != 0:
            return False
        stack = list(s)
        for i in stack:
            if i == '(':
                d = s.find(')')
                stack.pop(d)
                stack.remove(i)
            elif i == '{':
                return find(s, '}')
            elif i == '[':
                return find(s, ']')
        return True

        # return True


# Main funtion
if __name__ == '__main__':
    s = Solution()
    # print(s.scoreOfParentheses("(()))"))
    print(s.scoreOfParentheses("()(())"))