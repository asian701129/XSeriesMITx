# Enter your definitions for the SimpleVirus and Patient classes in this box.
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

        testForReporduced = random.random()
        if (testForReporduced <= self.maxBirthProb * (1 - popDensity)):
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
        self.virusCount = len(self.viruses)
        return self.virusCount


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
        # step 1
        current_count = self.getTotalPop()
        #print "We start with", current_count, "viruses"
        mark_for_removal = []
        for i in range(current_count):
            thisvirus = self.viruses[i]
            # if the virus gets cleared, mark for removal
            if (thisvirus.doesClear()):
                #print "We mark this virus."
                mark_for_removal.append(i)
                continue
            # if we don't remove it, just move on
            else:
                #print "We do not mark this virus."
                continue
        #for k in range(len(self.viruses)):
            #print "We have virus", k
        # make sure to remove them from the end to the front, otherwise you'll hit index errors
        for j in reversed(mark_for_removal):
            #print "We're going to try to remove virus in position", j
            self.viruses.pop(j)
        # step 2
        updated_current_count = self.getTotalPop()
        #print updated_current_count, " viruses are left after this update."
        
        currentPopDensity = updated_current_count/float(self.maxPop)        
        #print currentPopDensity, " is the concentration of viruses present."
        
        # step 3
        i = 0
        #edge case, if there are no viruses, then that is the new total pop
        if updated_current_count == 0:
            return 0
        else:
            #given this pop density, find out if if the virus reproduces or not
            for this in range(updated_current_count):
                try:
                    spawn = thisvirus.reproduce(currentPopDensity)
                    self.viruses.append(spawn)
                except NoChildException, e:
                    continue    
            return self.getTotalPop()
