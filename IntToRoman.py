class Solution(object):
    def intToRoman(self, num):
        _dict = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        rom = ''
        
        while num != 0:
            l = len(str(num))
            multiple = 10 ** (l-1)
            if num < 5 and num > 0:
                if num not in _dict.keys():
                    rom += _dict[multiple]
                else:
                    rom += _dict[num]
                    return rom
            else:
                multiple = (num // multiple) * multiple
                while multiple not in _dict.keys():
                    multiple -= -1
                rom += _dict[multiple]   
            num -= multiple
        return rom

# Main
if __name__ == '__main__':
    print(Solution().intToRoman(1994))