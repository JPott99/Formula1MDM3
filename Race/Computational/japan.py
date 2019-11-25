# Stats for Japan
import numpy as np
def course_stats():
    totalLaps = 53
    t_b = 90
    bonus = ["chassis","driver"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.10*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 19+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = np.exp(0.09*laps)-1
    elif type == "medium":
        p_t = 0.004*laps**2+0.65
    elif type == "hard":
        p_t = 1
    return p_t
