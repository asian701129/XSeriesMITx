class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"
        
    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        self.myCourseNames = []
        for course in courses:
            self.myCourses.append(courseInfo(course))
            self.myCourseNames.append(course)


    def getCourse(self, course):
        if (course in self.myCourseNames):
            index = self.myCourseNames.index(course)
            return self.myCourses[index]
        else:
            return
        
        

    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        #   fill in code to set the grade
        if not (grade > 0 and grade <= 100):
            return
        try:
            thiscourse = self.getCourse(course)
            return thiscourse.setGrade(grade)
        except:
            return

    def getGrade(self, course="6.02x"):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the grade
        if not (course in self.myCourseNames):
            return -1
        else:
            return self.getCourse(course).getGrade()


    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        
        if not (course in self.myCourseNames):
            return
        else:
            return self.getCourse(course).setPset(pset, score)

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        if not (course in self.myCourseNames):
            return -1
        else:
            return self.getCourse(course).getPset(pset)


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1,100)
edX.setPset(2,100,"6.00x")
edX.setPset(2,90,"6.00x")
edX.setGrade(100)

for c in ["6.00x","6.01x","6.02x"]:
    edX.setGrade(90,c)
