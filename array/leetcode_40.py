import copy


class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        combinations = []
        self.find_sum(candidates, target, -1, [], combinations)
        return combinations

    def find_sum(self, candidates, target, idx, combination, combinations):
        if target == 0:
            combinations.append(copy.copy(combination))
            return
        for i in range(idx + 1, len(candidates)):
            if i > idx + 1 and candidates[i] == candidates[i - 1]:
                continue
            if target - candidates[i] < 0:
                break
            combination.append(candidates[i])
            self.find_sum(candidates, target - candidates[i], i, combination, combinations)
            combination.remove(candidates[i])
