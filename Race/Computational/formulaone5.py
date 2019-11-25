import matplotlib.pyplot as plt
import sys

def tyre_type_l_max(tyre_type):
    if tyre_type == "soft":
        l_max = soft_l_max
    elif tyre_type == "medium":
        l_max = med_l_max
    elif tyre_type == "hard":
        l_max = hard_l_max
    else:
        print("Error: Not a Valid Tyre Type.")
    return l_max
def tyre_type_l_maxT(tyre_type):
    if tyre_type == "soft":
        l_max = soft_l_max_t
    elif tyre_type == "medium":
        l_max = med_l_max_t
    elif tyre_type == "hard":
        l_max = hard_l_max_t
    else:
        print("Error: Not a Valid Tyre Type.")
    return l_max
#Acceptable codes:
#aus        esp    mnc     bel      ita     hun       usa  jpn   cnd      brz
#Australia, Spain, Monaco, Belgium, Itally, Hunagary, USA, Japan, Canada, Brazil

#Financial Planning Weightings.
driveScore = 2.5
chassisScore = 0
engineScore = 6
#Set what tyres to use at each point (assume fuelled to next tyre pitstop)
# tyre_order = ['soft', 'soft', 'soft', 'soft', 'soft', 'soft', 'soft', 'soft', 'soft']
#tyre_order = ['hard', 'hard', 'hard', 'hard', 'hard', 'hard', 'hard', 'hard', 'hard']
#The number of seconds that tyres can add to laptime before a pitstop
tyre_tol = 0.7
#Note:  Some tracks have a constant value for hard tyres, so sometimes hard
#       tyres can go 0 laps (e.g Japan, where 1 second is added by hard tyres),
#       and sometimes they can go the entire course, which means that the car is
#       fuelled for the entire race at the start, which may not be possible.

#import data for the course specified by input (see above)
if __name__ == "__main__":
    course = sys.argv[1]
    if course == "aus":
        from australia import *
        course = "Australia"
        [soft_l_max,med_l_max,hard_l_max] = [14,18,20]
        tyre_order_a = ['hard', 'medium', 'hard']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [14,25,58]
        tyre_order_tt = ['medium', 'soft', 'medium']
    elif course == "esp":
        from spain import *
        [soft_l_max,med_l_max,hard_l_max] = [14,18,21]
        tyre_order_a = ['medium', 'medium', 'soft', 'medium']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [9,12,25]
        tyre_order_tt = ['hard', 'hard', 'hard']
        course = "Spain"
    elif course == "mnc":
        from monaco import *
        course = "Monaco"
        [soft_l_max,med_l_max,hard_l_max] = [16,21,24]
        tyre_order_a = ['hard', 'soft', 'soft', 'hard']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [13,25,78]
        tyre_order_tt = ['medium', 'medium', 'hard']
    elif course == "bel":
        from belgium import *
        course = "Belgium"
        [soft_l_max,med_l_max,hard_l_max] = [11,13,15]
        tyre_order_a = ['hard', 'hard', 'hard']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [9,12,18]
        tyre_order_tt = ['hard', 'medium', 'hard']
    elif course == "ita":
        from italy import *
        course = "Italy"
        [soft_l_max,med_l_max,hard_l_max] = [13,18,20]
        tyre_order_a = ['hard', 'soft', 'hard']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [10,16,53]
        tyre_order_tt = ['medium', 'medium', 'hard']
    elif course == "hun":
        from hungary import *
        course = "Hungary"
        [soft_l_max,med_l_max,hard_l_max] = [13,17,21]
        tyre_order_a = ['hard', 'soft', 'hard', 'medium']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [12,17,70]
        tyre_order_tt = ['medium', 'medium', 'medium', 'hard']
    elif course == "usa":
        from usa import *
        course = "USA"
        [soft_l_max,med_l_max,hard_l_max] = [12,13,16]
        tyre_order_a = ['hard', 'soft', 'hard', 'hard', 'hard', 'hard']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [10,12,18]
        tyre_order_tt = ['hard', 'hard', 'hard', 'hard', 'hard']
    elif course == "jpn":
        from japan import *
        course = "Japan"
        [soft_l_max,med_l_max,hard_l_max] = [12,14,20]
        tyre_order_a = ['hard', 'medium', 'hard']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [11,16,53]
        tyre_order_tt = ['medium', 'medium', 'hard']
    elif course == "cnd":
        from canada import *
        course = "Canada"
        [soft_l_max,med_l_max,hard_l_max] = [12,17,19]
        tyre_order_a = ['hard', 'hard', 'hard', 'medium']
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [11,22,70]
        tyre_order_tt = ['medium', 'soft', 'soft', 'soft', 'medium']
    elif course == "brz":
        from brazil import *
        course = "Brazil"
        [soft_l_max,med_l_max,hard_l_max] = [13,19,19]
        [soft_l_max_t,med_l_max_t,hard_l_max_t] = [10,10,25]
        tyre_order_tt = ['hard', 'hard', 'hard']
        tyre_order_a = ['hard', 'hard', 'hard', 'medium']
    else:
        print("Error: There is no track with that code.")
        exit()
#Initialise the simulation given the course.
if __name__ == "__main__":
    [totalLaps, t_b, bonus] = course_stats()
    #assign bonuses for the course
    cd = 1
    ce = 1
    cc = 1
    for i in bonus:
        if i == "engine":
            ce = 2
        if i == "chassis":
            cc = 2
        if i == "driver":
            cd = 2
    #Total Scores
    scoreTotal = 3*(cd*driveScore+cc*chassisScore+ce*engineScore)/(ce+cc+cd)

    tA = 0
    tT = 0

    #Random Variables in Racetime (for now averaged to zero)
    setupScore = 0
    R = 0 #Random per lap

    #
    #Find how long to use each tyre before a pit stop
    #
#The Race is run.
if __name__ == "__main__":
    ############################################################################
    #Starting Tyres
    ############################################################################
    startTyresA = tyre_order_a[0]
    ############################################################################
    tyre_typeA = startTyresA
    l_maxA = tyre_type_l_max(tyre_typeA)
    pitCountA = 0
    lapTimeA = 0
    lastPitLapA = 0
    lapsA = []
    lapCumalA = []
    startTyresT = tyre_order_tt[0]
    ############################################################################
    tyre_typeT = startTyresT
    l_maxT = tyre_type_l_maxT(tyre_typeT)
    pitCountT = 0
    lapTimeT = 0
    lastPitLapT = 0
    lapsT = []
    lapCumalT = []
    #Each loop is a lap
    for l in range(totalLaps):
        p_f_a = fuel_performance(l-lastPitLapA,l_maxA)
        p_f_t = fuel_performance(l-lastPitLapT,l_maxT)
        #If out of fuel, then use Pitstop.
        if l_maxA<=0:
            #If there are fewer laps then the maximum laps for a tyre type
            #then use the quickest tyres for the remaining time.
            ################################################################
                #algorithm/decision for choosing new tyres should go here
            ################################################################
            tyre_typeA = tyre_order_a[pitCountA+1]
            ################################################################
            if totalLaps-l<tyre_type_l_max(tyre_typeA):
                l_maxA = totalLaps-l
            else:
                l_maxA = tyre_type_l_max(tyre_typeA)
            t_pA = pit_time(l_maxA)
            lastPitLapA = l
            pitCountA+=1
        else:
            t_pA = 0

        if l_maxT<=0:
            #If there are fewer laps then the maximum laps for a tyre type
            #then use the quickest tyres for the remaining time.
            ################################################################
                #algorithm/decision for choosing new tyres should go here
            ################################################################
            tyre_typeT = tyre_order_tt[pitCountT+1]
            ################################################################
            if totalLaps-l<tyre_type_l_maxT(tyre_typeT):
                l_maxT = totalLaps-l
            else:
                l_maxT = tyre_type_l_maxT(tyre_typeT)
            t_pT = pit_time(l_maxT)
            lastPitLapT = l
            pitCountT+=1
        else:
            t_pT = 0
        p_tA = tyre_performance(l-lastPitLapA+1,tyre_typeA)
        p_tT = tyre_performance(l-lastPitLapT+1,tyre_typeT)
        t_perf = -0.15*(scoreTotal+setupScore)
        lapTimeA = t_b + t_perf + p_tA + p_f_a + R + t_pA
        lapTimeT = t_b + t_perf + p_tT + p_f_t + R + t_pT
        lapsA.append(lapTimeA)
        lapsT.append(lapTimeT)
        tA += lapTimeA
        tT += lapTimeT
        lapCumalA.append(tA)
        lapCumalT.append(tT)
        l_maxA -= 1
        l_maxT -= 1
    print("  The Racetime was for Analytical", str(round(tA,4))+"s.")
    print("  The Racetime was for Computational", str(round(tT,4))+"s.")
    fig,ax1 = plt.subplots()
    ax1.plot(lapsA)
    ax1.plot(lapsT)
    ax1.grid(1)
    ax1.set_xlabel("Lap")
    ax1.set_ylabel("Time(s)")
    ax1.legend(("Analytical","Computational"))
    fileString = ("graphs/"+course.lower()+"CompareRace.png")
    plt.savefig(fileString)
