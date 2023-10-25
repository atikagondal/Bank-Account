# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:30:16 2023

@author: atika
"""


#first we will import the important classes time and wraps from functools
import time
from functools import wraps
#defining the withdrawal decorator with func as argument which is supposed to see the amount if there is less than 0 then 
#we will see a message that says invalid amount
def withdrawal_decorator(func):
    @wraps(func)
    def wrapper(self,amount):
        if amount <=0:
            print(f"Invalid withdrawal amount.")
        elif amount >self.balance:
            print("Insufficient balance.")
        else:
            func(self,amount)#calling on the original function withdrawal
    return wrapper

# decorator on how much time a function takes when it runs

def measure_of_the_time(func):
    @wraps(func)
    def wrapper (self,*args):
        start_time=time.time()
        result=func(self,*args)
        end_time=time.time()
        print(f"Time taken for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

#defining the bankaccount class
class BankAccount:
    def __init__(self, account_number, initialbalance):
        self.account_number = account_number
        self.balance = initialbalance
        self.transaction_history = []  # creates an empty list to store my or the accounts transaction history
        self.is_closed = False   # adding the self.is_closed and set it to False as standard

#creating a method register transactions which will register the time and the values we want it to look at
    def register_transaction(self,transaction_type, amount):
            timestamp=time.strftime("%Y-%m-%d  %H:%M:%S")
            self.transaction_history.append({
                "timestamp":timestamp,
                "type":transaction_type,
                "amount":amount
                })
            
    #setting a deposit decorater which will only run the time function takes and the deposit function
    @measure_of_the_time
    def deposit(self, amount):
        if self.is_account_closed():
            print("Error: Cannot deposit to a closed account.")
        else:
            # if the amount is greater than 0 then it will be added in the account
            if amount > 0:
                self.balance += amount 
                self.register_transaction("deposit", amount)
    
    #setting a withdrawal decorater which will  also run the time function and withdrawaldecorator 
    @withdrawal_decorator
    @measure_of_the_time
    def withdraw(self, amount):
        if self.is_account_closed():
            print("Error: Cannot withdraw from a closed account.")
        elif amount <= 0:
             print("Error: invalid amount")
        elif amount > self.balance:
             print ("Insuffient balance")
        self.balance -= amount
        self.register_transaction("withdrawal", amount)
        
    #get balance method
    def get_balance(self):
            return self.balance
        
    #get transaction_history method
    def get_transaction_history(self):
            return self.transaction_history    
    
    #defining the close_account method
    def close_account(self):
        self.is_closed=True
        self.balance =0
        self.transaction_history.clear()
        #del self

    def is_account_closed(self):
        #print(f"Checking if the account is closed. Balance: {self.balance}, Transaction History: {self.transaction_history}")
        #return self.balance == 0 and not self.transaction_history
        return self.is_closed

        #return self.balance==0 

        
#Create a function menu 

def menu():

    print("Welcome to my bankaccount managemnet \n")
    print("1. Create an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check my accounts balance")
    print("5. Accounts transactions history")
    print("6. Account statement")
    print("7. Account summary")
    print("8. Close account")
    

    print("9. Check if my account is closed")

    print("10. Exit")
    


#menubased control
menu()
choice=int(input("Choose your option => \n"))
while choice >= 1 and choice <= 9:
    
    if choice ==1:
        
        account_number=input("Create your account ")
        initialbalance=float(input("Write in your balance "))
        account = BankAccount(account_number,initialbalance)
       # account.deposit(initialbalance)
        
        print(f"Account with account number: {account_number} and with {initialbalance} in your account\n")
       
    elif choice ==2:
        deposit_amount=float(input("How much do you want to deposit "))
        account.deposit(deposit_amount)
        print(f"{deposit_amount} was deposited in your account")
        
    
    elif choice ==3:
        uttak=float(input("How much do you want to withdraw from your account "))
        account.withdraw(uttak)
        print(f" The required amount {uttak} has been withdrawed \n")
        
    elif choice ==4:
        print(f"Balance of this account is {account.get_balance()}\n ")
    
    elif choice ==5:
        history=account.get_transaction_history()
        print("Transaction history:\n")
        for transaction in history:
            print(f"{transaction['timestamp']} - {transaction['type']}: {transaction['amount']}\n")
    
    elif choice == 6:
        print("Account Statement\n")
        print(f"Account Number: {account.account_number}\n")
        print(f"Current Balance: {account.get_balance()}\n")
        print("Transaction History:\n")
        for transaction in account.get_transaction_history():
            print(f"{transaction['timestamp']} - {transaction['type']}:{transaction['amount']}\n")

    elif choice == 7:
        print("Account summary\n")
        print(f"Account Number: {account.account_number}\n")
        print(f"Current balance: {account.get_balance()}\n")
        print(f"Number of transactions: {len(account.get_transaction_history())}\n")
        
   
    elif choice == 8:
        if account is not None:
            account.close_account()
            is_closed = True  # Merk at kontoen er stengt
            print("Account is closed, and the transaction list is cleared and set to zero.")
        else:
            print("Error: No account exists, create an account first.")

    elif choice == 9:
        if account is None:
            print("Error: No account exists.")
        elif account.is_closed:
            print("The account is closed.")
        else:
            print("The account is still open")
    
    

    print("\n")
    menu()
    
    choice=int(input("\nSkriv inn et ønsket tall for prosjektet =>\n"))
    '''
if account.is_account_closed():
    print("stengt")
        
'''
print("Closing the program. Goodbye")
    
        
        
        