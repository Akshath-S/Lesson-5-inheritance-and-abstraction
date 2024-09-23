class person():
    def __init__(self,Name,idnumber):
        self.Name=Name
        self.idnumber=idnumber
    def display(self):
        print(self.Name,self.idnumber)

class employee(person):
    def __init__(self, Name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,Name,idnumber)

a=employee("Ram",123123123123,2000000000,"Ceo")
a.display()

        