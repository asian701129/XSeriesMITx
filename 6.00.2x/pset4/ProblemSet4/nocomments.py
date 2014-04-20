# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    def prepData(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):
        finalPops = [ [], [], [], [] ]
        for trial in range(numTrials):
            for updateCounter in enumerate([300, 150, 75, 0]):
            #for updateCounter in enumerate([0]):
                viruses = []
                for i in range(numViruses):
                    viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
                #print "I start my simulation with", len(viruses)
                aPatient = TreatedPatient(viruses, maxPop)

                for i in range(updateCounter[1]):
                    aPatient.update()
                aPatient.addPrescription('guttagonol')
                for i in range(150):
                    print
                    print aPatient.getTotalPop()
                    aPatient.update()
                
                finalPop = aPatient.getTotalPop()
                #print finalPop
                finalPops[updateCounter[0]].append(finalPop)
                
        return finalPops
        

    def plotData(finalVirusPopulations, whichHist):
        pylab.figure()
        pylab.hist(finalVirusPopulations[whichHist], 5)
        
        if whichHist == 0:
            num = 300
        elif whichHist == 1:
            num = 150
        elif whichHist == 2:
            num = 75
        if whichHist == 3:
            num = 0
        pylab.title("Final Virus Populations with virus present for " + str(num) + " seconds before Medicine")
        pylab.xlabel("Final Virus Populations")
        pylab.ylabel("Number of Trials")
        #pylab.legend()
        pylab.show()


    def returnAnswer(finalVirusPopulations):
        counts = [0,0,0,0]
        for a in [0,1,2,3]:
            finalVirusPopulations[a].sort()
            count = 0
            for i in range(len(finalVirusPopulations[a])):
                if finalVirusPopulations[a][i] >= 0 and finalVirusPopulations[a][i] <= 50:
                    count += 1
                else:
                    continue
            counts[a] = count
        print "There were", counts, "trials where between 0 and 50 were left out of", numTrials,"total trials"
        return counts

    allTheData = prepData(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials)

    plotData(allTheData,0) #300
    plotData(allTheData,1) #150
    plotData(allTheData,2) #75
    plotData(allTheData,3) #0

    return returnAnswer(allTheData)

simulationDelayedTreatment(50)