import random

def sampleQuizzes():
    '''
    returns: the probability of a student with final score between 70 and 75
    given the distrubution of the tests:
    M1 between 50 and 80
    M2 between 60 and 90
    F1 between 55 and 95
    and
    M1 weighs 0.25    
    M2 weighs 0.25
    F1 weighs 0.50
    '''
    finalscores = genScoreList(10000)
    studentsInRange = 0
    for score in finalscores:
        if (score >= 70.0 and score <= 75.0):
            studentsInRange += 1 
    prob = float(studentsInRange)/float(len(finalscores))
    return prob

class Student(object):
    '''
    a student 
    '''
    def __init__(self):
        self.scores = []
        self.scores.append(random.choice(range(50,81)))
        self.scores.append(random.choice(range(60,91)))
        self.scores.append(random.choice(range(55,96)))
        self.finalgrade = self.scores[0]*0.25 + self.scores[1]*0.25 + self.scores[2]*0.50
        #print self.scores
        #print self.finalgrade
    
    def getFinalGrade(self):
        return self.finalgrade

def genScoreList(n):
    '''
    returns: a list of length n containing Student's final scores as entries
    '''
    finalscores = []    
    for i in range(n):
        finalscores.append(Student().getFinalGrade())
    finalscores.sort()
    return finalscores
