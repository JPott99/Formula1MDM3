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
        tyre_tol = 0.7
        tyre_order = ['medium', 'soft', 'medium']
    elif course == "esp":
        from spain import *
        tyre_tol = 0.7
        tyre_order = ['hard', 'hard', 'hard']
        course = "Spain"
    elif course == "mnc":
        from monaco import *
        course = "Monaco"
        tyre_tol = 1
        tyre_order = ['medium', 'medium', 'hard']
    elif course == "bel":
        from belgium import *
        course = "Belgium"
        tyre_tol = 1.4
        tyre_order = ['hard', 'medium', 'hard']
    elif course == "ita":
        from italy import *
        course = "Italy"
        tyre_tol = 0.9
        tyre_order = ['medium', 'medium', 'hard']
    elif course == "hun":
        from hungary import *
        course = "Hungary"
        tyre_tol = 1.2
        tyre_order = ['medium', 'medium', 'medium', 'hard']
    elif course == "usa":
        from usa import *
        course = "USA"
        tyre_tol = 1
        tyre_order = ['hard', 'hard', 'hard', 'hard', 'hard']
    elif course == "jpn":
        from japan import *
        course = "Japan"
        tyre_tol = 1.6
        tyre_order = ['medium', 'medium', 'hard']
    elif course == "cnd":
        from canada import *
        course = "Canada"
        tyre_tol = 0.7
        tyre_order = ['medium', 'soft', 'soft', 'soft', 'medium']
    elif course == "brz":
        from brazil import *
        course = "Brazil"
        tyre_tol = 0.6
        tyre_order = ['hard', 'hard', 'hard']
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

    t = 0

    #Random Variables in Racetime (for now averaged to zero)
    setupScore = 0
    R = 0 #Random per lap

    #
    #Find how long to use each tyre before a pit stop
    #
    soft_l_max = 0
    med_l_max = 0
    hard_l_max = 0
    for l in range(totalLaps):
        if tyre_performance(l,"soft")<tyre_tol:
            soft_l_max+=1
        if tyre_performance(l,"medium")<tyre_tol:
            med_l_max+=1
        if tyre_performance(l,"hard")<tyre_tol:
            hard_l_max+=1
    print("  The maximum laps for soft tyres are", str(soft_l_max) + ".")
    print("  The maximum laps for medium tyres are", str(med_l_max) + ".")
    print("  The maximum laps for hard tyres are", str(hard_l_max) + ".")
#The Race is run.
if __name__ == "__main__":
    ############################################################################
    #Starting Tyres
    ############################################################################
    startTyres = tyre_order[0]
    ############################################################################
    tyre_type = startTyres
    l_max = tyre_type_l_max(tyre_type)
    print("  Starting on",tyre_type,"tyres with",l_max,"laps of fuel.")
    pitCount = 0
    lapTime = 0
    lastPitLap=0
    laps = []
    lapCumal = []
    #Each loop is a lap
    for l in range(totalLaps):
        p_f = fuel_performance(l-lastPitLap,l_max)
        #If out of fuel, then use Pitstop.
        if l_max<=0:
            #If there are fewer laps then the maximum laps for a tyre type
            #then use the quickest tyres for the remaining time.
            ################################################################
                #algorithm/decision for choosing new tyres should go here
            ################################################################
            tyre_type = tyre_order[pitCount+1]
            ################################################################
            if totalLaps-l<tyre_type_l_max(tyre_type):
                l_max = totalLaps-l
            else:
                l_max = tyre_type_l_max(tyre_type)
            t_p = pit_time(l_max)
            lastPitLap = l
            pitCount+=1
            print("  Pitstop",pitCount,"after",l,"laps to",tyre_type,"tyres with",l_max,"laps of fuel for",t_p,"seconds"+".")
        else:
            t_p = 0
        p_t = tyre_performance(l-lastPitLap+1,tyre_type)
        t_perf = -0.15*(scoreTotal+setupScore)
        lapTime = t_b + t_perf + p_t + p_f + R + t_p
        laps.append(lapTime)
        t += lapTime
        lapCumal.append(t)
        if len(sys.argv)>2:
            if sys.argv[2] == "--laps":
                print("LAP",str(l)+":",lapTime)
        l_max -= 1
    print("  The Racetime was", str(round(t,4))+"s.")
    if len(sys.argv)>2:
        if sys.argv[2] == "--plot":
            fig,ax1 = plt.subplots()
            ax1.plot(laps)
            ax1.grid(1)
            ax1.set_xlabel("Lap")
            ax1.set_ylabel("Time(s)")
            fileString = ("graphs/"+course.lower()+"OptimalRace.png")
            plt.savefig(fileString)
