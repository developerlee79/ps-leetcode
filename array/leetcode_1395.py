class Solution(object):
    def numTeams(self, rating):
        n = len(rating)
        teams = 0
        for i, rate in enumerate(rating):
            left_less, left_more = self.find_less_and_more(rating, 0, i, rate)
            right_less, right_more = self.find_less_and_more(rating, i + 1, n, rate)
            teams += left_more * right_less + left_less * right_more
        return teams

    @staticmethod
    def find_less_and_more(nums, start, end, target):
        less = 0
        more = 0
        for i in range(start, end):
            if nums[i] < target:
                less += 1
            elif nums[i] > target:
                more += 1
        return less, more
