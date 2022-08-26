# // Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# // You may assume that each input would have exactly one solution, and you may not use the same element twice.
# // You can return the answer in any order.



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
#       Loop through the array
#       Add Every element num[x] with the next element num[x+1]
#       Check if num[x]+num[x+1] == target
#       Add indexOf(x) and indexOf(x+1) to result
#       Return result

        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result


    # Main
    def main(self):
        nums = [3,2,4]
        target = 6
        print(self.twoSum(nums, target))


# Run
if __name__ == '__main__':
    Solution().main()
    