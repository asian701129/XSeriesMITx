# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        testForCleared = random.random()
        if (testForCleared <= self.getClearProb()):
            return True
        return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        testForReproduced = random.random()
        if (testForReproduced <= self.maxBirthProb * (1 - popDensity)):
            #cause reproduction
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            #raise exception
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.virusCount = len(viruses)
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)


    def removeViruses(self):
        '''
        Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        '''
        currentVirusCount = self.getTotalPop()
        #print "We start with", currentVirusCount, "viruses, and some will die."

        # look at every virus initially present, and mark some of them to be removed
        mark_for_removal = []
        for i in range(currentVirusCount):
            thisvirus = self.viruses[i]
            # if the virus gets cleared, mark for removal
            if (thisvirus.doesClear()):
                #print "We mark this virus for removal."
                mark_for_removal.append(i)
                continue
            # if we don't remove it, just move on
            else:
                #print "We do not mark this virus for removal."
                continue
        #for k in range(len(self.viruses)):
        #    print "We have virus", k
            
        # actually remove the viruses which we marked to be removed
        # make sure to remove them from the end to the front
        # otherwise you'll hit index errors
        for j in reversed(mark_for_removal):
            #print "We're going to try to remove virus in position", j
            self.viruses.pop(j)
    
    def calcPopDens(self):
        '''
        The current population density is calculated. This population density
        value is used until the next call to update()
        '''
        virusesRemaining = self.getTotalPop()        
        currentPopDensity = virusesRemaining/float(self.maxPop)
        #print virusesRemaining, " viruses are left after this update."    
        #print currentPopDensity, " is the concentration of viruses present."
        return currentPopDensity
        
    def spawnVirues(self, currentPopDensity):
        '''
        Based on this value of population density, determine whether each 
        virus particle should reproduce and add offspring virus particles to 
        the list of viruses in this patient. 
        '''
        virusesRemaining = self.getTotalPop()
        #print virusesRemaining, "viruses survived the purge, and some will reproduce."
        #edge case, if there are no viruses, then we spawn nothing
        if virusesRemaining == 0:
            return
        new_viruses = []
        #given this pop density, find out if if the virus reproduces or not
        for i in range(virusesRemaining):
            thisvirus = self.viruses[i]    
            try:
                spawn = thisvirus.reproduce(currentPopDensity)
                self.viruses.append(spawn)
            except NoChildException, e:
                continue

        #for k in range(len(self.viruses)):
        #    print "We have virus", k
            
        # add the reproduced viruses to the patient's body
        for j in new_viruses:
            #print "We're going to add the new virus from position", j
            self.viruses.push(j)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        self.removeViruses()
        currentPopDensity = self.calcPopDens()        
        self.spawnVirues(currentPopDensity)        
        return self.getTotalPop()



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    # TODO
    def prepData():
        virusPopAverager = []
        for i in range(300):
            virusPopAverager.append(0.0)
    
        for trial in range(numTrials):
            viruses = []
            for i in range(numViruses):
                viruses.append(SimpleVirus(maxBirthProb, clearProb))
            aPatient = Patient(viruses, maxPop)
            
            virusPopPerTime = []
            for i in range(300):
                aPatient.update()
                pop = aPatient.getTotalPop()
                #print pop
                virusPopPerTime.append(pop)
            for i in range(300):
                virusPopAverager[i] += virusPopPerTime[i]
        
        for i in range(300):
            virusPopAverager[i] /= float(numTrials)
        return virusPopAverager
    
    def plotData(virusPopAverager):
        pylab.figure()
        pylab.plot(range(300),virusPopAverager)
        pylab.title("Average Virus Population Vs Time")
        pylab.xlabel("Time Elapsed")
        pylab.ylabel("Average Virus Population")
        pylab.legend()
        pylab.show()
    
    virusPopAverager = prepData()
    plotData(virusPopAverager)


#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        # TODO
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        # TODO
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        if drug in self.resistances:
            return self.resistances[drug]
        else:
            return False

    def detChildResistances(self):
        childResistances = {}
        
        # consider each drug the parent has a resistance to (or not)
        for aDrug in self.resistances.keys():

            testForMutation = random.random()

            if (testForMutation <= (1.0 - self.mutProb)):
                # the resistance is inherited same as the parent
                childResistances[aDrug] = self.resistances[aDrug]
            else:
                # the resistance is mutated, opposite the parent
                childResistances[aDrug] = not self.resistances[aDrug]

            #print childResistances
            
        return childResistances

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO
        # look at each drug in the list of drugss applied
        for aDrug in activeDrugs:
            if self.isResistantTo(aDrug):
                # the virus can resist this drug, move on to the next drug
                continue
            else:
                # the virus cannot resist this drug, so the drug stops reproduction
                raise NoChildException
        
        # the virus was able to resist all the drugs, it might reproduce
        # See if random reproduction occurs
        testForReproduced = random.random()
        if (testForReproduced <= self.maxBirthProb * (1 - popDensity)):
            #cause reproduction
            childResistances = self.detChildResistances()            
            return ResistantVirus(self.maxBirthProb, self.clearProb, childResistances, self.mutProb)
        
        else:
            #no reproduction, raise exception
            raise NoChildException
            
            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        # TODO
        Patient.__init__(self, viruses, maxPop)
        self.currentDrugs = []
        

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        # TODO
        if not newDrug in self.currentDrugs:
            self.currentDrugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO
        return self.currentDrugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """

        # TODO
        # look at each virus
        resistantVirusCount = 0
        for aVirus in self.viruses:
            flag = True
            # look at each drug in the list
            for aDrug in drugResist:
                if aVirus.isResistantTo(aDrug):
                    continue
                else:
                    flag = False
                    break
            # it was resistant to every single drug
            if flag:
                resistantVirusCount += 1
        return resistantVirusCount
                    
    def removeViruses(self):
        '''
        Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        '''
        currentVirusCount = self.getTotalPop()
        #print "We start with", currentVirusCount, "viruses, and some will die."

        # look at every virus initially present, and mark some of them to be removed
        mark_for_removal = []
        for i in range(currentVirusCount):
            thisvirus = self.viruses[i]
            # if the virus gets cleared, mark for removal
            if (thisvirus.doesClear()):
                #print "We mark this virus for removal."
                mark_for_removal.append(i)
                continue
            # if we don't remove it, just move on
            else:
                #print "We do not mark this virus for removal."
                continue
        #for k in range(len(self.viruses)):
        #    print "We have virus", k
            
        # actually remove the viruses which we marked to be removed
        # make sure to remove them from the end to the front
        # otherwise you'll hit index errors
        for j in reversed(mark_for_removal):
            #print "We're going to try to remove virus in position", j
            self.viruses.pop(j)
    
    def calcPopDens(self):
        '''
        The current population density is calculated. This population density
        value is used until the next call to update()
        '''
        virusesRemaining = self.getTotalPop()        
        currentPopDensity = virusesRemaining/float(self.maxPop)
        #print virusesRemaining, " viruses are left after this update."    
        #print currentPopDensity, " is the concentration of viruses present."
        return currentPopDensity
        
    def spawnVirues(self, currentPopDensity):
        '''
        Based on this value of population density, determine whether each 
        virus particle should reproduce and add offspring virus particles to 
        the list of viruses in this patient. 
        '''
        virusesRemaining = self.getTotalPop()
        #print virusesRemaining, "viruses survived the purge, and some will reproduce."
        #edge case, if there are no viruses, then we spawn nothing
        if virusesRemaining == 0:
            return
        new_viruses = []
        #given this pop density, find out if if the virus reproduces or not
        for i in range(virusesRemaining):
            thisvirus = self.viruses[i]    
            try:
                spawn = thisvirus.reproduce(currentPopDensity, self.currentDrugs)
                self.viruses.append(spawn)
            except NoChildException, e:
                continue

        #for k in range(len(self.viruses)):
        #    print "We have virus", k
            
        # add the reproduced viruses to the patient's body
        for j in new_viruses:
            #print "We're going to add the new virus from position", j
            self.viruses.push(j)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        self.removeViruses()
        currentPopDensity = self.calcPopDens()        
        self.spawnVirues(currentPopDensity)        
        return self.getTotalPop()
        


#
# PROBLEM 5
#
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
        virusPopAverager = []
        resistantVirusPopAverager = []
        for i in range(num+num2):
            virusPopAverager.append(0.0)
        for i in range(num+num2):
            resistantVirusPopAverager.append(0.0)
            
            
        for trial in range(numTrials):
            viruses = []
            for i in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            aPatient = TreatedPatient(viruses, maxPop)
            
            virusPopPerTime = []
            resistantVirusPopPerTime = []
            
            
            
            for i in range(num):
                aPatient.update()
                pop = aPatient.getTotalPop()
                #print pop
                virusPopPerTime.append(pop)
                rpop = aPatient.getResistPop(['guttagonol'])
                #print rpop
                resistantVirusPopPerTime.append(rpop)
    
            aPatient.addPrescription('guttagonol')
    
            for i in range(num2):
                aPatient.update()
                pop = aPatient.getTotalPop()
                #print pop
                virusPopPerTime.append(pop)
                rpop = aPatient.getResistPop(['guttagonol'])
                #print rpop
                resistantVirusPopPerTime.append(rpop)
            for i in range(num+num2):
                virusPopAverager[i] += virusPopPerTime[i]
    
            for i in range(num+num2):
                resistantVirusPopAverager[i] += resistantVirusPopPerTime[i]
            
        for i in range(num+num2):
            virusPopAverager[i] /= float(numTrials)
    
        for i in range(num+num2):
            resistantVirusPopAverager[i] /= float(numTrials)
        
        print "Final Virus Pop (total) is", aPatient.getTotalPop()
        print "Final Virus Pop (reisistant) is", aPatient.getResistPop(['guttagonol'])
        return [virusPopAverager,resistantVirusPopAverager]
        
    def plotData(virusPopAverager,resistantVirusPopAverager,num,num2):
        pylab.figure()
        pylab.plot(range(num+num2),virusPopAverager)
        pylab.plot(range(num+num2),resistantVirusPopAverager)
        pylab.title("Average Virus Population Vs Time")
        pylab.xlabel("Time Elapsed")
        pylab.ylabel("Average Virus Population")
        pylab.legend()
        pylab.show()

    twoplots = prepData(150,150)
    plotData(twoplots[0],twoplots[1],150,150)
#simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,mutProb, numTrials):
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 5)