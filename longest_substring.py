# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == j - i:
                    longest = max(longest, j - i)
                else:
                    break
        return longest

