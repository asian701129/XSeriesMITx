import random
def detChildResistances(self):
    childResistances = {}
    
    # consider each drug the parent has a resistance to (or not)
    for drugNames in self.resistances.keys():

        testForMutation = random.random()

        if (testForMutation <= (1.0 - self.mutProb)):
            # the resistance is inherited same as the parent
            childResistances[drugNames] = self.resistances[drugNames]
        else:
            # the resistance is mutated, opposite the parent
            childResistances[drugNames] = not self.resistances[drugNames]

        print childResistances
        
    return childResistances
