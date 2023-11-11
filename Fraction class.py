class Fraction:
    
    def __init__ (self , n , d ):
        self.num = n
        self.den = d
       
        
    def __str__ (self):
        return "{}/{}".format(self.num , self.den)
       
    
    # def __add__ (self):
    #     return "{}+{}".format(self.num , self.den)
    
    # def __mul__ (self):
    #     return "{}*{}".format(self.num , self.den)
        
    
    # def __add__ (self , other):
    #     temp_num = self.num * other.den + other.num * self.den
    #     temp_den = self.den * other.den
        
    #     return "{}/{}".format(temp_num , temp_den)
   
    # def __sub__ (self , other):
    #     temp_num = self.num * other.den - other.num * self.den
    #     temp_den = self.den * other.den
        
    #     return "{}/{}".format(temp_num , temp_den)
    
    # def __mul__ (self , other):
    #     temp_num = self.num * other.num
    #     temp_den = self.den * other.den
        
    #     return "{}/{}".format(temp_num , temp_den)
    
    def __truediv__(self , other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        
        return "{}/{}".format(temp_num , temp_den)
    
    
n = int(input("Enter 1st numeritor: "))
d = int(input("Enter 1st denominator: "))  
n1 = int(input("Enter 2nd numeritor: "))
d2 = int(input("Enter 2nd denominator: "))  
p1 = Fraction(n , d)
p2 = Fraction(n1 , d2)

print(p1)
print(p2)
# print(p1 + p2)
# print(p1 - p2)
# print(p1 * p2)
print(p1/p2)