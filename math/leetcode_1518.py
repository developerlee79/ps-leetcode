class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottle_count = numBottles
        i = numBottles
        while i >= numExchange:
            bottle_count += int(i / numExchange)
            i = int(i / numExchange) + (i % numExchange)
        return bottle_count
