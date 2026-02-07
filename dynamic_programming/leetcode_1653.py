class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        before = 0

        for ch in s:
            if ch == 'b':
                before += 1
            elif before:
                deletions += 1
                before -= 1

        return deletions
