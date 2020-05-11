import sys
from pathlib import Path

p = Path(__file__).parents[1]
sys.path.append(str(p))

from ex_3 import Solution

def test_lengthOfLongestSubstring1():
    input = 'abcabcbb'
    result = Solution().lengthOfLongestSubstring(input)
    assert result == 3

def test_lengthOfLongestSubstring2():
    input = 'bbbbb'
    result = Solution().lengthOfLongestSubstring(input)
    assert result == 1

def test_lengthOfLongestSubstring3():
    input = 'pwwkew'
    result = Solution().lengthOfLongestSubstring(input)
    assert result == 3


