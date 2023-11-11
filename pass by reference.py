class Customer:
    
    def __init__ (self , name , gender):
        self.name = name 
        self.gender = gender
        
def greet(customer):
    if customer.gender == "Female":
        print("Hello" , customer.name , "Mam")
    else:
        print("Hello" , customer.name , "Sir")
        
    
    cust2 = Customer("Alina" , "Female")
    return cust2
        

cust = Customer("Alisha" , "Male")
# greet(cust)

new_cust = greet(cust)
print(new_cust.gender)