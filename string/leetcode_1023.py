class Solution(object):
    def camelMatch(self, queries, pattern):
        answer = []

        for query in queries:
            answer.append(self.is_match(query, pattern))

        return answer

    @staticmethod
    def is_match(query, pattern):
        n = len(pattern)
        pi = 0

        for i, ch in enumerate(query):
            if pi < n and ch == pattern[pi]:
                pi += 1
            elif ch.isupper():
                return False

        return pi == n
