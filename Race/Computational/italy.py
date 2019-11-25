# Stats for Italy
import numpy as np
def course_stats():
    totalLaps = 53
    t_b = 85
    bonus = ["engine"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.11*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 21+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = np.exp(0.07*laps)-1
    elif type == "medium":
        p_t = 0.14*laps**0.5+0.35
    elif type == "hard":
        p_t = 0.7
    return p_t
