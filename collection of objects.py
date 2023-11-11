############################Collection of objects########################################

class Customer:
    
    def __init__ (self , name , age):
        self.name = name
        self.age = age
        
    
    def intro(self):
        print("Hello" , "my name is" , self.name , "My age is" , self.age)
        

p1 = Customer("Alisha" , 20)
p2 = Customer("Seerat" , 21)
p3 = Customer("Aroosa" , 19)

L1 = [p1 , p2 , p3]

for i in L1:
    #print(i.name , i.age)
    
    i.intro()
    
    