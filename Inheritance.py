class person:                           #base class
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def fullnameage(self):                 #base class function
        print(f"{self.fname} {self.lname} {self.age}")
        

class student(person):
    def __init__(self,fname,lname,age):
        person.__init__(self,fname,lname)   #or use super().__init__(fname,lname) here self not required
        self.age = age
        
    def __str__(self):
        return f"{self.fname},{self.lname},{self.age}"
        
def main():
    s1 = student('Lokesh','Punwani',22)
    s1.fullnameage()
    return 0
    
main()
