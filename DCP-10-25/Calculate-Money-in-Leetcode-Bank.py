class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        left = n % 7

        total = 0

        for i in range(weeks):
            total += (i * 7) + 28
        
        if (left > 0):
            starting = weeks + 1
            for i in range(left):
                total += starting
                starting += 1

        return total


