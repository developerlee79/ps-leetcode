class Solution(object):
    def distributeCandies(self, candies, num_people):
        candies_distribution = [0] * num_people

        left_candies = candies
        candy = 1

        while left_candies > 0:
            candies_distribution[candy % num_people - 1] += min(candy, left_candies)
            left_candies -= candy
            candy += 1

        return candies_distribution
