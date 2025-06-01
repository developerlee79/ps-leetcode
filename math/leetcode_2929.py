class Solution(object):
    def distributeCandies(self, n, limit):
        answer = 0
        i = 0
        while i <= limit:
            start = max(n - i - limit, 0)
            end = n - i
            if start <= limit and start <= end:
                answer += min(end, limit) - start + 1
            i += 1
        return answer
