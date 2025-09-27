class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        n = len(intervals)
        prev = 0
        count = 1 # non overlapping intervals

        #[[1,2],[2,3],[3,4],[1,3]]
        #[[1,2],[1,3],[2,3],[3,4]]

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]: # no overlap
                count += 1
                prev = i

        return n - count
            
        
