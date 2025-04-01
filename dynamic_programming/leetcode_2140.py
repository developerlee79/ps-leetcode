class Solution(object):
    def mostPoints(self, questions):
        dp = [0] * len(questions)
        self.find_max_point(questions, dp, 0, 0)
        return dp[0]

    def find_max_point(self, questions, dp, index, curr_points):
        if index >= len(questions):
            return curr_points
        if dp[index] > 0:
            return dp[index] + curr_points
        points, brainpower = questions[index]
        take_points = self.find_max_point(questions, dp, index + brainpower + 1, points)
        skip_points = self.find_max_point(questions, dp, index + 1, 0)
        dp[index] = max(take_points, skip_points)
        return dp[index] + curr_points
