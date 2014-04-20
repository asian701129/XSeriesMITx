import pylab
from sampleQuizzes import *

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    
def plotQuizzes():
    '''
    plots a historgram
    '''
    myscores = genScoreList(10000)
    
    
    pylab.figure()    
    #pylab.plot(xvalues,yvalues)
    pylab.hist(myscores,7)
    
    pylab.title("Distribution of Scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    
    pylab.show()