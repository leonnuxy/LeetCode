class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


# Main funtion
if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["fleower", "fleow", "fleight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))