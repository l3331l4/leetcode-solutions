from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # Write your code here
        # [1,2,5,6],[1,3],[4,10]
        flattened = []

        for i in schedule:
            for j in range(0, len(i), 2):

                flattened.append([i[j], i[j+1]])

        flattened.sort(key=lambda x: x[0])
        print(flattened)
        merged = []

        prev = flattened[0]
        n = len(flattened)

        for j in range(1, n):
            curr = flattened[j]
            if prev[1] >= curr[0]:
                prev[0] = min(prev[0], curr[0])
                prev[1] = max(prev[1], curr[1])
                continue
            else:
                merged.append(prev)
                prev = flattened[j]

        merged.append(prev)
        
        print(merged)

        freetime = []
        prev = merged[0]

        for i in range(1, len(merged)):
            curr = merged[i]
            if prev[1] < curr[0]:
                freetime.append(Interval(prev[1], curr[0]))
                prev = curr

        return freetime


