# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

from pip import main


class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        pairs = {'(':')'} # Pairing of parentheses 
        stack = []  # Stack to store the parentheses
        score = 0 # Score of the string
        for i in s: 
            print (i)
                


# Main funtion
if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfParentheses("(())"))
    print("New")
    print(s.scoreOfParentheses("(()(()))"))