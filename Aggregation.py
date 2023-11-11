class Customer:
    
    def __init__ (self , name , gender , age , address , personal_info):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address
        self.personal_info = personal_info
    
class Address:
    
    def __init__ (self , city , state , country):
        self.city = city
        self.state = state
        self.country = country

class Personal_info:
    
    def __init__ (self , father_name , mother_name ):
        self.father_name = father_name
        self.mother_name = mother_name
        

per_info = Personal_info("Sultan" , "Asma")
add = Address("Lahore" , "Punjab" , "Pakistan")
cust = Customer("Alisha" , "Female" , 20 , add , per_info)

print(cust.personal_info.mother_name)
