def sort_key(interval):
    return interval[0]
def merge_intervals(intervals):
    intervals.sort(key=sort_key)

    merged = []
    currtent = intervals[0]
    merged.append(currtent)
    for interval in intervals:
        if interval[0] <= currtent[1]:
            currtent[1] = max(currtent[1], interval[1])
        else:
            merged.append(interval)
            currtent = interval
    return merged
  


intervals = [
    [1,3],
    [8,10],
    [2,6],
    [15,18],
    [9,12]
]

result = merge_intervals(intervals)
print("Merged intervals:", result)