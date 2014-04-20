import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

pylab.figure()
pylab.plot(xVals, yVals)
pylab.show()

pylab.figure()
pylab.plot(xVals, zVals)
pylab.show()

pylab.figure()
pylab.plot(sorted(xVals), yVals)
pylab.show()

pylab.figure()
pylab.plot(xVals, sorted(yVals))
pylab.show()

pylab.figure()
pylab.plot(sorted(xVals), sorted(yVals))
pylab.show()
