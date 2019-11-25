import matplotlib.pyplot as plt
import sys
import numpy as np

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

s = "soft"
m = "medium"
h = "hard"
tyre_orders =[

[s,s,s],[m,m,m],[h,h,h],
[s,s,m],[s,m,s],[m,s,s],
[s,s,h],[s,h,s],[h,s,s],
[m,m,h],[m,h,m],[h,m,m],
[m,m,s],[m,s,m],[s,m,m],
[s,m,h],[s,h,m],[m,h,s],
[h,m,s],[h,s,m],[m,s,h],
[h,h,m],[h,m,h],[m,h,h],
[h,h,s],[h,s,h],[s,h,h]

]

#import data for the course specified by input (see above)
if __name__ == "__main__":

    course = sys.argv[1]
    if course == "aus":
        from australia import *
        [soft_l_max,med_l_max,hard_l_max] = [14,18,20]
    elif course == "esp":
        from spain import *
        [soft_l_max,med_l_max,hard_l_max] = [14,18,21]
    elif course == "mnc":
        from monaco import *
        [soft_l_max,med_l_max,hard_l_max] = [16,21,24]
    elif course == "bel":
        from belgium import *
        [soft_l_max,med_l_max,hard_l_max] = [11,13,15]
    elif course == "ita":
        from italy import *
        [soft_l_max,med_l_max,hard_l_max] = [13,18,20]
    elif course == "hun":
        from hungary import *
        [soft_l_max,med_l_max,hard_l_max] = [13,17,21]
    elif course == "usa":
        from usa import *
        [soft_l_max,med_l_max,hard_l_max] = [12,13,16]
    elif course == "jpn":
        from japan import *
        [soft_l_max,med_l_max,hard_l_max] = [12,14,20]
    elif course == "cnd":
        from canada import *
        [soft_l_max,med_l_max,hard_l_max] = [12,17,19]
    elif course == "brz":
        from brazil import *
        [soft_l_max,med_l_max,hard_l_max] = [13,19,19]
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
    #R is random per lap
    R = 0


#The Race is run.
if __name__ == "__main__":
    minTime = 1e99
    minTimeList = []
    bestTyres = []
    t_list = []
    for i in tyre_orders:
        for j in tyre_orders:
            for k in tyre_orders:
                tyre_order = [i[0],i[1],i[2],j[0],j[1],j[2],k[0],k[1],k[2]]
                ############################################################################
                #Starting Tyres
                ############################################################################
                startTyres = tyre_order[0]
                ############################################################################
                tyre_type = startTyres
                l_max = tyre_type_l_max(tyre_type)
                #print("  Starting on",tyre_type,"tyres with",l_max,"laps of fuel.")
                pitCount = 0
                lapTime = 0
                lastPitLap = 0
                t=0
                #Each loop is a lap
                for l in range(totalLaps):
                    p_f = fuel_performance(l-lastPitLap,l_max)
                    #If out of fuel, then use Pitstop.
                    if l_max<=0:
                        #If there are fewer laps then the maximum laps for a tyre type
                        #then use the quickest tyres for the remaining time.
                        ################################################################
                        ################################################################
                        if pitCount+1 < len(tyre_order):
                            tyre_type = tyre_order[pitCount+1]
                        else:
                            t = 6e3
                            break
                        ################################################################
                        if totalLaps-l<tyre_type_l_max(tyre_type):
                            l_max = totalLaps-l
                        else:
                            l_max = tyre_type_l_max(tyre_type)
                        if l_max == 0:
                            t = 6e3
                            break
                        t_p = pit_time(l_max)
                        lastPitLap = l
                        pitCount+=1
                        #print("  Pitstop",pitCount,"after",l,"laps to",tyre_type,"tyres with",l_max,"laps of fuel for",t_p,"seconds"+".")
                    else:
                        t_p = 0
                    p_t = tyre_performance(l-lastPitLap+1,tyre_type)
                    t_perf = -0.15*(scoreTotal+setupScore)
                    lapTime = t_b + t_perf + p_t + p_f + R + t_p
                    t += lapTime
                    l_max -= 1
                #print("  The Racetime was", str(round(t,4))+"s.")
                if t < minTime:
                    minTime = t
                    bestTyres = tyre_order
                    minTimeList = []
                elif t == minTime:
                    if tyre_order[0:pitCount+1] not in minTimeList:
                        minTimeList.append(tyre_order[0:pitCount+1])
                t_list.append(t)
    #print(bestTyres)
    for i in minTimeList:
        print("The best tyre sequence is",i)
    print("This configuration took",minTime, "seconds.")
    #plt.scatter(range(len(t_list)),t_list,s=1)
    #plt.show()
