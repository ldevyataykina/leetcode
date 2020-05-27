from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = sorted(nums1 + nums2)
        if len(result) % 2 != 0:
            return result[len(result) // 2]
        else:
            return (result[len(result) // 2 - 1] + result[len(result) // 2]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            # need to reverse lists and their lengths. J may be negative
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        i_min, i_max, half_len = 0, m, (m + n + 1) / 2
        print(half_len)
        while i_min <= i_max:
            i = (i_min + i_max) / 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is to small. Need to increase it
                i_min += 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big. Need to reduce it
                i_max -= 1
            else:
                # i is ok
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if m == n: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0




if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2, 9, 13, 18, 21], [3, 4, 6, 9, 11, 190]))
    print(Solution().findMedianSortedArrays2([1, 2, 9, 13, 18, 21], [3, 4, 6, 9, 11, 190]))