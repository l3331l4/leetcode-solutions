class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles

        empty = numBottles
        full = 0

        for i in range(1, numBottles+1):
            if (i % numExchange) == 0:
                empty -= numExchange
                full += 1
        
        while full:
            drank += 1
            full -= 1
            empty += 1

            if (empty % numExchange) == 0:
                empty -= numExchange
                full += 1

        return drank
            

            

                


