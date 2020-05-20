import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    !!! The fist Solution is 15% faster than Solution2 !!!

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Return a ListNode of sum of every 2 numbers from l1 and l2
        :param l1: the first linked list
        :param l2: the second linked list
        :return: ListNode of sum input numbers
        """
        res_1 = str(l1.val)
        res_2 = str(l2.val)

        while l1.next:
            l1 = l1.next
            res_1 += str(l1.val)

        while l2.next:
            l2 = l2.next
            res_2 += str(l2.val)

        res = str(int(res_1[::-1]) + int(res_2[::-1]))
        output = None
        for i in res:
            print(int(i), output)
            output = ListNode(val=int(i), next=output)

        return output

class Solution2:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Return a ListNode of sum of every 2 numbers from l1 and l2
        :param l1: the first linked list
        :param l2: the second linked list
        :return: ListNode of sum input numbers
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            val_1 = val_2 = 0
            if l1:
                val_1 = l1.val
                l1 = l1.next
            if l2:
                val_2 = l2.val
                l2 = l2.next
            carry, val = divmod(val_1 + val_2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


if __name__ == "__main__":
    start = time.time()
    print(Solution().addTwoNumbers(ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None))),
                                   ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))))
    print(f'Total time: {time.time() - start}')