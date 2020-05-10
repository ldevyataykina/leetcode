from copy import deepcopy


class Solution:
    """
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sums to target.
    """

    def combinationFind(self, results, combination, candidates, target, ind):
        """
        :type results: List[List[int]]
        :type combination: List[int]
        :type candidates: List[int]
        :type target: int
        :type ind: int
        """
        if target == 0:
            results.append(deepcopy(combination))

        for i in range(ind, len(candidates)):
            if candidates[i] > target:
                break

            combination.append(candidates[i])
            self.combinationFind(results, combination, candidates, target - candidates[i], i)
            combination.pop(len(combination) - 1)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        results = []
        combination = []
        self.combinationFind(results, combination, candidates, target, 0)
        return results


if __name__ == "__main__":
    result = Solution()
    print(result.combinationSum([2, 3, 6, 7], 7))