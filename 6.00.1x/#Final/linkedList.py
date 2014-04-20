class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name


def insertBefore(atMe, newFrob, backFrob):
    #we look backwards until we find the proper location or the beginning of the list
    myFrobsName = newFrob.myName()
    while (1):
        backFrobName = backFrob.myName()
        # my frob goes directly between the current and the one before it, so insert it there
        if myFrobsName >= backFrobName:
            newFrob.setBefore(backFrob)
            newFrob.setAfter(atMe)
            backFrob.setAfter(newFrob)
            atMe.setBefore(newFrob)
            return
        # my frob goes further back in the chain, so go further back and check things out there
        else:
            tempFrob = backFrob.getBefore()
            if tempFrob == None:
                #we are inserting at the very beginning
                newFrob.setAfter(backFrob)
                backFrob.setBefore(newFrob)
                return
            else:
                atMe = backFrob
                backFrob = tempFrob
            
def insertAfter(atMe, newFrob, frontFrob):
    #we look forwards until we find the proper location or the end of the list
    myFrobsName = newFrob.myName()
    while (1):
        frontFrobName = frontFrob.myName()
        # my frob goes directly between the current and the one after it, so insert it there
        if myFrobsName <= frontFrobName:
            newFrob.setBefore(atMe)
            newFrob.setAfter(frontFrob)
            atMe.setAfter(newFrob)
            frontFrob.setBefore(newFrob)
            return
        # my frob goes further forward in the chain, so go forward and check things out there
        else:
            tempFrob = frontFrob.getAfter()
            if tempFrob == None:
                #we are inserting at the very end
                newFrob.setBefore(frontFrob)
                frontFrob.setAfter(newFrob)
                return
            else:
                atMe = frontFrob
                frontFrob = tempFrob

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links?
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """

    currentLocationName = atMe.myName()
    myFrobsName = newFrob.myName()

    backFrob = atMe.getBefore()
    frontFrob = atMe.getAfter()
    
    
    if backFrob == None and frontFrob == None:
        if myFrobsName <= currentLocationName:
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
            return
        elif myFrobsName >= currentLocationName:
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
            return
        
    
    if backFrob == None:
        #if the name is before or the same as the current name, the new frob starts the list
        if myFrobsName <= currentLocationName:
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
            return
        else:
            insertAfter(atMe, newFrob, frontFrob)
            return
    
    
    if frontFrob == None:
        #if the name is identical or greater than the current name, put it after the current one
        if myFrobsName >= currentLocationName:
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
            return
        else:
            insertBefore(atMe, newFrob, backFrob)
            return
           
    # newFrob goes somewhere behind the location we're given
    if myFrobsName < currentLocationName:
        insertBefore(atMe, newFrob, backFrob)
        return

    # newFrob goes somewhere after the location we're given
    if myFrobsName >= currentLocationName:
        insertAfter(atMe, newFrob, frontFrob)
        return
    
    return
