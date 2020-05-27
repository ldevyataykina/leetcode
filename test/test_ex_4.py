import sys
from pathlib import Path

p = Path(__file__).parents[1]
sys.path.append(str(p))

import pytest
from ex_4 import Solution

def findMedianSortedArrays1():
    input = [[1, 3], [2]]
    result = Solution().findMedianSortedArrays(input[0], input[1])
    assert result == 2.0

def findMedianSortedArrays2():
    input = [[1, 2], [3, 4]]
    result = Solution().findMedianSortedArrays(input[0], input[1])
    assert result == 2.5
