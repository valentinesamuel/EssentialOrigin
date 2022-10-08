class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

rooms = [(0,30), (5, 10), (15,20)]
def meeting_rooms(interval):
    interval.sort(lambda i: i.start)
    for i in range(1, len(interval)):
        interval1 = interval[i-1]
        interval2 = interval[i]

        if interval1.end < interval2.start:
            return True
    return False
    
#  leetcode 252
    
    
    