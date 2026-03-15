#Merge Overlapping intervals

def mergeintervals(intervals):
    if not intervals:
        return []
#Step1 : Sort Intervals by start time
    intervals.sort()
    merged = []

n = int(input().strip())
intervals = []
for i in range(n):
    s, e = map(int,input().split())
    intervals.append([s,e])
result = mergeintervals(intervals)
for s,e in result:
    print(s,e)