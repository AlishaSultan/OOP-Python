class Login:
    
    def login(self):
        print("Login")
    
    def signup(self):
        print("signup")
        

class Student(Login):             ############inheritance##################
    
    def name(self):
        print("Alisha")
        
    def age(self):
        print(23)
        
    def gender(self):
        print("Female")
        

stu = Student()
stu.login()
stu.signup()
stu.name()
stu.age()