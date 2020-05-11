class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        max_n = 0

        for letter in s:
            if letter not in result:
                result += letter
            else:
                result = result[result.find(letter) + 1:] + letter

            max_n = max(max_n, len(result))

        return max_n