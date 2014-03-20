import pylab

def processTemps():
    '''
    processes the file given to us
    '''
    inFile = open('C:/Users/Anthony/Dropbox/XSeriesMITx/6.00.2x/Lecture1/julyTemps.txt', 'r')
    lowlist = []
    highlist = []
    for line in inFile:        
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            highlist.append(int(fields[1]))
            lowlist.append(int(fields[2]))
    return (lowlist,highlist)

var = processTemps()

low = var[0]
high = var[1]
diffTemp = []

for i in range(len(high)):
    temp = high[i] - low[i]
    print temp
    diffTemp.append(temp)
    
pylab.plot(range(1,32), diffTemp)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')
pylab.show()