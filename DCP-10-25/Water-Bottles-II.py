class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        drank += numBottles
        full = 0
        empty = numBottles

        exchange = numExchange

        while empty >= exchange:
            full += 1
            empty -= exchange
            exchange += 1

        while full:            
            drank += full
            empty += full
            full = 0
            while empty >= exchange:
                full += 1
                empty -= exchange
                exchange += 1
        
        return drank


            