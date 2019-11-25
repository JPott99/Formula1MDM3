# Stats for Belgium
import numpy as np
def course_stats():
    totalLaps = 44
    t_b = 105
    bonus = ["chassis","engine"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.13*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 19+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = np.exp(0.1*laps)-1
    elif type == "medium":
        p_t = 0.006*laps**2+0.55
    elif type == "hard":
        p_t = 0.04*laps + 0.7
    return p_t
