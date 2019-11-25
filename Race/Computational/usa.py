# Stats for United States
import numpy as np
def course_stats():
    totalLaps = 88
    t_b = 63
    bonus = ["engine"]
    return [totalLaps, t_b, bonus]

def fuel_performance(laps,laps_max):
    p_f = 0.13*(laps_max)
    return p_f

def pit_time(laps_max):
    t_p = 21+0.5*laps_max
    return t_p

def tyre_performance(laps, type):
    if type == "soft":
        p_t = 0.01*laps**2+0.005*laps
    elif type == "medium":
        p_t = 0.006*laps**2 + 0.003*laps + 0.2
    elif type == "hard":
        p_t = 0.002*laps**2 + 0.001*laps + 0.4
    return p_t
