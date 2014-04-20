from ps3b import *


'''
problem 2
'''
#virus = SimpleVirus(1.0, 0.0)
#patient = Patient([virus], 100)

#virus = SimpleVirus(1.0, 1.0)
#patient = Patient([virus], 100)

viruses = [ SimpleVirus(0.68, 0.93), SimpleVirus(0.36, 0.95), SimpleVirus(0.14, 0.9), SimpleVirus(0.41, 0.78) ]
P1 = Patient(viruses, 8)
P1.getTotalPop()

number = P1.update()
print number



'''
problem 3
'''

simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)


'''
problem 4
'''
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
patient = TreatedPatient([virus1, virus2], 1000000)
patient.addPrescription("drug1")
patient.update()
patient.update()

'''
problem 5
'''
simulationWithDrug(100, 1000, 0.1, 0.05, 100)