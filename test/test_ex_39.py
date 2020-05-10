import sys
from pathlib import Path
import pytest

p = Path(__file__).parents[1]
sys.path.append(str(p))

from ex_39 import Solution

def test_CombinationSum1():
    input = [2, 3, 6, 7]
    target = 7
    result = Solution().combinationSum(input, target)
    assert sorted(result) == sorted([[2,2,3],[7]])

def test_CombinationSum2():
    input = [2, 3, 5]
    target = 8
    result = Solution().combinationSum(input, target)
    assert sorted(result) == sorted([[2,2,2,2], [2,3,3], [3,5]])

def test_CombinationSum3():
    input = [7, 3, 2]
    target = 18
    result = Solution().combinationSum(input, target)
    assert sorted(result) == sorted([[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,3,7],[2,2,2,3,3,3,3],[2,2,7,7],
                                     [2,3,3,3,7],[3,3,3,3,3,3]])

def test_CombinationSum4():
    input = [4, 5, 2]
    target = 16
    result = Solution().combinationSum(input, target)
    assert sorted(result) == sorted([[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,4],[2,2,2,2,4,4],[2,2,2,5,5],[2,2,4,4,4],
                                     [2,4,5,5],[4,4,4,4]])

def test_CombinationsSum5():
    input = [3, 2, 8]
    target = 18
    result = Solution().combinationSum(input, target)
    assert sorted(result) == sorted([[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,2,8],[2,2,2,3,3,3,3],[2,2,3,3,8],
                                     [2,8,8],[3,3,3,3,3,3]])