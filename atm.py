class atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print('your balance is 50000: ')
    def withdrawl(self,amount):
        new_amount=50000-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
def main():
    card_number=input('insert card')
    pin_number=input('enter your pin')
    new_user=atm(card_number,pin_number)
    print('chose your activity')
    print("1.Balance Enquriy 2.withdrawl")
    activity = int(input("enter activity number :- "))
    if (activity == 1): 
        new_user.check_balance() 
    elif (activity == 2): 
        amount = int(input("enter the amount:- ")) 
        new_user.withdrawl(amount) 
    else:
         print("enter a valid number")
if __name__ == "__main__":
    main()
        