# Stats for Monaco
import numpy as np
def course_stats():
    totalLaps = 78
    t_b = 74
    bonus = ["driver"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.06*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 17+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = 0.08 * laps
    elif type == "medium":
        p_t = 0.12*laps**0.5 + 0.4
    elif type == "hard":
        p_t = 0.8
    return p_t
