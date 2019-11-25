# Stats for Australia
import numpy as np
def course_stats():
    totalLaps = 58
    t_b = 84
    bonus = ["none"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.08*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 16+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = 0.004*(laps)**2
    elif type == "medium":
        p_t = 0.02*laps + 0.2
    elif type == "hard":
        p_t = 0.4
    return p_t
