####################################Constructor Executed###############################

# class Phone:
    
#     def __init__ (self , phone , brand , Price):
#         print("Constructor Executed")
#         self.phone = phone
#         self.brand = brand
#         self.Price = Price
        

# class Smartphone(Phone):
#     pass

# s1 = Smartphone("I-phone" , "Apple" , "$20000")
# print(s1.phone)
# print(s1.brand)
# print(s1.Price)


#####################################is it access private members##########################

# class Phone:
    
#     def __init__ (self , phone , brand , Price):
#         print("Constructor Executed")
#         self.phone = phone
#         self.__brand = brand
#         self.Price = Price
        

# class Smartphone(Phone):
#     pass

# s1 = Smartphone("I-phone" , "Apple" , "$20000")
# #print(s1.phone)
# print(s1.__brand)
# #print(s1.Price)


######################################### Which method run#################################

# class Phone:
    
#     def __init__ (self , phone , brand , Price):
#         print("Constructor Executed")
#         self.phone = phone
#         self.__brand = brand
#         self.Price = Price
        
#     def buy(self):
#         print("Buy your phone")

# class Smartphone(Phone):
    
#     def buy(self):
#         print("Buy your Smartphone")         ###########method overriding################3
    

# s1 = Smartphone("I-phone" , "Apple" , "$20000")
# s1.buy()



class Phone:
    
    def __init__ (self , phone , brand , Price):
        print("Constructor Executed")
        self.phone = phone
        self.__brand = brand
        self.Price = Price
        
    def buy(self):
        print("Buy your phone")

class Smartphone(Phone):
    
    def buy(self):
        print("Buy your Smartphone")###########method overriding################
        super().buy()
    

s1 = Smartphone("I-phone" , "Apple" , "$20000")
s1.buy()


    
    
    
        

