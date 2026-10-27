class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        answer = []
        for i in range(m - 1):
            row = ['#'] * n
            row[0] = '.'
            answer.append(''.join(row))
        answer.append(''.join(['.'] * n))

        return answer
