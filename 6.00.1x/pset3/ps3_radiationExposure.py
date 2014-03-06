#def f(x):
#    return x^2+2*x+2

def f(x):
	import math
	return 400*math.e**(math.log(0.5)/3.66 * x)


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    totalWidth = stop - start
    rectangleCount = totalWidth/step
    print (str(rectangleCount))
    area = 0
    
    for i in range(int(rectangleCount)):
        area = area + f(start + i*step)*step
    
    return area

radiationExposure(0, 4, 0.25)