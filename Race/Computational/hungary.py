# Stats for Hungary
import numpy as np
def course_stats():
    totalLaps = 70
    t_b = 80
    bonus = ["chassis"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.08*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 18+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = np.exp(0.07*laps)-1
    elif type == "medium":
        p_t = 0.05*laps+0.35
    elif type == "hard":
        p_t = 0.8
    return p_t
