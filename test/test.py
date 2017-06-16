class Student(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def printStudent(self):
        print("name: %s, id: %s" % (self.name,self.id))

class Student2(Student):
    pass

s2 = Student2("DTY","3140104431")
s2.printStudent()

dir(s2)