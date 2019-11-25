# Stats for Spain
import numpy as np
def course_stats():
    totalLaps = 66
    t_b = 80
    bonus = ["none"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.09*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 20+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = np.exp(0.06*laps)-1
    elif type == "medium":
        p_t = 0.04*laps+0.25
    elif type == "hard":
        p_t = 0.02*laps**0.5 + 0.6
    return p_t
