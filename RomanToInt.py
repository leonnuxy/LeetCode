class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        _dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in range(len(s)):
            x = _dict[s[i]]
            # Meant to add the next number if the previous number is smaller than the current number
            # This to count the given Roman numemral as a single number
            if i == len(s) - 1:                 # If i is the last element
                num += _dict[s[i]]               # Add the last element
            elif _dict[s[i]] < _dict[s[i+1]]:     # If the current element is smaller than the next element
                num -= _dict[s[i]]               # Subtract the current element
            else:                 # If current element is larger than next element or equal to next element
                num += _dict[s[i]]               # Add the current element
        return num


# Main
if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))


