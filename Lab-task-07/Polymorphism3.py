class Person:    
    def __init__(self, a, b):
        print("Person Constructor")        
        self.f_name = a        
        self.l_name = b
    
    def display(self):        
        print("Your First name : ", self.f_name)        
        print("Your last name : ", self.l_name)

class Student(Person):
    def __init__(self, a, b, s_year):
        print("Student constructor")
        Person.__init__(self, a, b)
        self.s_year = s_year

    def display(self):
        print("Hello", self.f_name, self.l_name, ". Congrats for your graduation in the year", self.s_year)

class Teacher(Person):
    def __init__(self, a, b, t_year):
        print("Teacher constructor")
        Person.__init__(self, a, b)
        self.t_year = t_year

    def display(self):
        print("Presenting respecter teacher", self.f_name, self.l_name, ". Congrats for your joining in the year", self.t_year)

class Admin(Person):
    def __init__(self, a, b, a_year):
        print("Admin constructor")
        Person.__init__(self, a, b)
        self.a_year = a_year

    def display(self):
        print("Hello", self.f_name, self.l_name, ". Congrats for your joining in the year", self.a_year)
class Current_Student(Student):
    def __init__(self, a, b, s_year, id):
        print("current_Student constructor")
        Student.__init__(self, a, b, s_year)
        self.id = id

    def display(self):
        print("Hello", self.f_name, self.l_name,"id ", self.id, ".You will be graduate in", self.s_year)
class Alumni_Student(Student):
    def __init__(self, a, b, s_year, id):
        print("Alumni_Student constructor")
        Student.__init__(self, a, b , s_year)
        self.id = id

    def display(self):
        print("Hello", self.f_name, self.l_name, "id ", self.id ,". Congrats for your graduation in the year", self.s_year)

class Employee(Teacher,Admin):
    def __init__(self, a, b, t_year):
        print("Employee Constructor")
        super().__init__(a, b, t_year)
S1 = Current_Student("Negar", "Sultana", 2026 , 1813)
S1.display()
S2 = Alumni_Student("Negar", "sultana", 2026 , 3439)
S1.display()
E1 = Employee("Nasima Islam", "Bithi", 2020)
T1 = Teacher("Nasima islam", "Bithi", 2020)
T1.display()
A1 = Admin("Mina", "Khatun", 2014)
A1.display()