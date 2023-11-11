import sys

class Atm:
    
    
    counter = 1              #######Static Method##############
    
    def __init__ (self):
        self.__pin = ""                     ### Encapsulation###
        self.__balance = 0.0
        self.sno = Atm.counter
        Atm.counter = Atm.counter + 1
        
        print(id(self))
        
    @staticmethod

    def get_counter():
        print(Atm.counter)
        
    @staticmethod  
 
    def Set_counter(new):
        if type(new) == int:
           Atm.counter = new
           print(Atm.counter)
            
        
       
    def menu(self):
        print("Enter your choice: ")
        "\n"
        user_input = input("""
          1. Enter 1 to create pin
          2. Enter 2 to deposit
          3. Enter 3 to withdraw
          4. Enter 4 to check balance
          5. Enter 5 to exit
""")
       
        
        if user_input == '1':
              self.create_pin()
        elif user_input == '2':
             self.deposit()
        elif user_input == '3':
             self.withdraw()
        elif user_input == '4':
             self.check_balance()
        else:
             print("exit")
             
    
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("You entered pin successful😊")
        
    #######################  Setter or getter ###################################
    

   
    def get_pin(self):
        print("Your updated pin is: " , self.__pin)
    
    def Set_pin(self):
        new_pin = input("Press Y if u want to change and if not then Press N: ")
        if new_pin == 'Y':
            new_pin = input("Please Enter new pin: ")
            self.__pin = new_pin
            print("Your Pin has been changed")
        else:
            p1.deposit()
            
            

        
    def deposit(self):
        pin_enter = input("Enter your pin: ")
        if pin_enter == self.__pin:
            
            deposit_amount = float(input("Enter your amount which u want to deposit:"))
            self.__balance = deposit_amount + self.__balance
            print("Your updted balance is:" , self.__balance)
            print("You entered your deposit amount successfully😍")
        else:
            print("You entered pin wrong please try again!")
            sys.exit()
        

    def withdraw(self):
        pin_enter = input("Enter your pin: ")
        if pin_enter == self.__pin:
            
            withdraw_amount = float(input("Enter your withdraw amount:"))
            if self.__balance >= withdraw_amount:
               self.__balance = self.__balance - withdraw_amount
               print("You withdrawal balance successfully👍")
            elif self.__balance < withdraw_amount:
         
               print("YOur balance is low.....!😢")
               sys.exit() 
            
        else:
              print("You entered pin wrong please try again!")  
              sys.exit()
             
       
             
    def check_balance(self):
        pin_enter = input("Enter your pin: ")
        if pin_enter == self.__pin:
           
            print("Your balance is:" , self.__balance)
        else:
             print("You entered pin wrong please try again!")
             sys.exit()
        
    
    
p1 = Atm()
# print(p1.sno)
p2 = Atm()
# print(p2.sno)
# p3 = Atm()
# print(p3.sno)
p1.get_counter()
p1.Set_counter(8)
#print(Atm.counter)
#print(p3.counter)
# p1.menu()
# p1.Set_pin()
# p1.get_pin()

# p1.withdraw()
# p1.check_balance()





    