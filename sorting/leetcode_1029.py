class Solution(object):
    def twoCitySchedCost(self, costs):
        count = len(costs) / 2
        a_count = count
        b_count = count
        min_cost = 0
        cost_diff = self.construct_diff(costs)
        for i in range(len(costs)):
            a, b = costs[cost_diff[i][1]]
            if a < b:
                if a_count > 0:
                    min_cost += a
                    a_count -= 1
                else:
                    min_cost += b
                    b_count -= 1
            else:
                if b_count > 0:
                    min_cost += b
                    b_count -= 1
                else:
                    min_cost += a
                    a_count -= 1
        return min_cost

    @staticmethod
    def construct_diff(costs):
        cost_diff = []
        for i, cost in enumerate(costs):
            a, b = cost
            cost_diff.append((-abs(a - b), i))
        cost_diff.sort()
        return cost_diff
