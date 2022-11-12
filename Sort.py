# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Case 1: list1 is None
        if list1 is None:
            return list2
        # Case 2: list2 is None
        if list2 is None:
            return list1
        # Case 3: list1 and list2 are not None
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def main():
    a = [1,3,4]
    b = [1,2,4]

    s = Solution()
    print(s.mergeTwoLists(a, b))


if __name__ == '__main__':
    main()
    