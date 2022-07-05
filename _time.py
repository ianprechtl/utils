import time

def ceil_time(seconds : float, time_sec : float = None) -> float:
    '''
    ex, ceil_time(1,100.4) = 101
    ex, ceil_time(2,100.4) = 102
    '''
    if not time_sec:
        time_sec = time.time()
    return time_sec + seconds - time_sec % seconds

def floor_time(seconds : float, time_sec : float = None) -> float:
    '''
    ex, floor_time(1,100.4) = 100
    ex, ceil_time(2,100.4) = 100
    '''
    if not time_sec:
        time_sec = time.time()
    return time_sec - time_sec % seconds