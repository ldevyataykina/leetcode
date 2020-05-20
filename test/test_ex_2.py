import sys
from pathlib import Path

p = Path(__file__).parents[1]
sys.path.append(str(p))

import pytest
from ex_2 import Solution, ListNode

def test_addTwoNumbers_1():
    input = [ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None))),
             ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))]
    result = Solution().addTwoNumbers(input[0], input[1])
    answer = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8, next=None)))
    result_list = []
    answer_list = []
    while result or answer:
        result_list.append(result.val)
        answer_list.append(answer.val)
        result = result.next
        answer = answer.next
    assert result_list == answer_list