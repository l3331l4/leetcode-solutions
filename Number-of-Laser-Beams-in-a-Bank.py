class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        noDevice = set()
        dev = {}
        n = len(bank)
        total = 0

        for i in range(n):
            devices = 0
            for c in bank[i]:
                if c == '1':
                    devices += 1
            if devices == 0:
                noDevice.add(i)
            dev[i] = devices

        for i in range(n):
            if dev[i] != 0:
                j = i + 1
                while j in dev and dev[j] == 0:
                    j += 1
                if j not in dev:
                    continue
                total += dev[i] * dev[j]

        return total
                

        
        
        

                