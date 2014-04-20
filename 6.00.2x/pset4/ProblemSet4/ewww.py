
import numpy
import random
import pylab
from ps3b import *
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    def prepData(num,num2):
        virusPopFinal = []
            
        for trial in range(numTrials):
            viruses = []
            for i in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            aPatient = TreatedPatient(viruses, maxPop)
            
            for i in range(num):
                aPatient.update()

            aPatient.addPrescription('guttagonol')
    
            for i in range(num2):
                aPatient.update()
            
            virusPopFinal.append(aPatient.getTotalPop())
    
            print "Final Virus Pop (total) is", aPatient.getTotalPop()
            print "Final Virus Pop (reisistant) is", aPatient.getResistPop(['guttagonol'])
        return virusPopFinal
        
    def plotData(virusPopFinal):
        pylab.figure()
        pylab.hist(virusPopFinal,5)
        pylab.title("Average Virus Population Vs Time")
        pylab.xlabel("Time Elapsed")
        pylab.ylabel("Average Virus Population")
        pylab.legend()
        pylab.show()

    virusPopFinal = prepData(150,150)
    plotData(virusPopFinal)

#simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,mutProb, numTrials):
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 5)