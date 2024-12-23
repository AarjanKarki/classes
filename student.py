class Student():
    name=''
    age=12
    schoolclass='6a'
    classteacher='Miss Mair'
    
    def __init__(self):
        print('making a new student')
    
    def changedetails(self):
        print('the details of the students are')
        self.age=int(input())
        print('please enter the name of the student')
        self.name=(input())
    def show_details(self):
        print('the details of the students are:')
        print('Name:',self.name)
        print('Age:',self.age)
        print('class:',self.schoolclass)
        print('house:', self.house)
        print('Classteacher:',self.classteacher)
        Arnav=Student()
        John=Student()
        Arnav.changedetails()
        Arnav.show_details()

