class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        



# Main
if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([1,1,2,2,3,3,4,4,5,5]))
    
