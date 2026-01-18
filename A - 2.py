class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age 

    def display(self):
        print(self.name)
        print(self.age)

class emp(Person):
    def __init__(self,name,age,salary,post):
        self.salary = salary 
        self.post = post 
        Person.__init__(self,name,age)

e1 = emp("Samarsh",23,25000,"Intern")
e1.display()
print("Salary: ",e1.salary)
print("Post: ",e1.post)

class emp2(Person):
    def __init__(self,name,age,salary,post):
        self.salary = salary 
        self.post = post 
        Person.__init__(self,name,age)

e1 = emp2("\nMax",23,30000,"Team Manager")
e1.display()
print("Salary: ",e1.salary)
print("Post: ",e1.post)