class BankAccount:
   
  def __init__(self, first_name, last_name, phone_Number, bank):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_Number = phone_Number
    self.bank = bank
    self.balance = 0
    self.withdrawals = []
    self.deposits = []
    self.loan_balance = 0

  def account_name(self):

    name = "{} account for {} {}".format(self.bank, self.first_name, self.last_name, self.phone_number, self.bank)
    return name

  def deposit(self, amount):
    try:
      amount+1
    except TypeError:
      print("You must enter the amount in figures")
      return
      
    if amount <= 0:   
      print("You cannot deposit zero or negative")
    else:
      self.balance += amount
      time = datetime.now()
      deposit = {
        "time": time,
       "amount": amount
         }
          self.deposit.append(deposit)
          formatted_time=strftime("%A, %drd %B %Y,%H:%M %p")
          print("You have deposited {} to {}".format(amount, self.account_name()))
            
            
          
    
  def withdraw(self, amount):
    try: 
      amount + 1
    except TypeError:
      print("Please enter the amount in figures")
        return
    if amount <= 0:
        print("You cannot withdraw zero or negative")
    elif amount > self.balance:
        print("You don't have enough balance")
    else:
        self.balance += amount
          time = datetime.now()
          deposit = {
            "time": time,
            "amount": amount
          }
          self.withdrawal.append(withdrawal)
          
          print("Dear {} you have withrawn {} from {}.Your current account balance is {}".format(self.account_name(),amount,get_time,self.balance))
          

  def get_balance(self):
    return "The balance for {} is {}".format(self.account_name(), self.balance,get_time)

  def show_deposit_statement(self):
    for deposit in deposits:
      time = datetime['time']
        amount = deposit['amount']
        print(statement)
            

  def show_withdrawal_statements(self):
    for withdraw in withdrawals:
      time = datetime['time']
            
    if amount<= 0:
      print("You cannot request for loan of that amount")
        
    else: 
      self.loan = amount
      print("You have been given loan of {}".format (amount)

  def request_loan(self,amount):
    try:
      amount +10
    except TypeError:
      print("Please enter the request amount in figures")
      return
    if amount <=0:
      print("You can not request a loan of that amount")
    else:
      self.loan = amount
      print("You have been given a loan of {}". format(amount))

      
  def repay_loan(self, amount):
    try:
      amount + 10
    except TypeError:
      print("Enter the repayment amount in figures")
      return

      if amount<= 0:
        print("You cannot repay with that amount")
      elif self.loan == 0:
        print("You don't have loan at the moment")
        elif amount > self.loan:
          print("Your loan is {}, please enter amount that is less or equal to the amount")
        else:
        print(" You have repayed your loan with {}.your loan balance is{}".format(mount))
      
  def loan_repayment_statement(self):
    for repayment in self.loan_repayment:
      time = repayment['time']
      amount = repayment['amount']
      formatted_time = self.get_formatted_time(time)
      statement = "You repaid {} on {}".format(amount,formatted_time)
      print(statement)

class BankAccount(Account):
  def__init__ (self,first_name,last_name,phone_number,bank):
    self.bank = bank
    supper().__init__(first_name,last_name_number) 


class MobileMoneyAccount(Account):
  def__init__ (self,first_name,last_name,phone_number,service_provider):
  self.service_provider = service_provider
  self.artime = []
  self.bill = []
  self.money = []
  supper().__init__(first_name,last_name_number)

  def buy_airtime(self,amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter the amount in figures")
      return
    if amount > self.balance:
      print("You don't have enough balance. Your balance is {}".format(self.balance))
    else:
      self.balance -= amount
      time=datetime.now()
      artime = {
        'time':time'
        'artime': amount:
      }
      self.airtime.append(airtime)
      print("You have bout airtime worth {} on ".format(amount,self.get_formatted_time(time))

def pay_bill(self,amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter the amount in figures")
      return
    if amount > self.balance:
      print("You don't have enough balance. Your balance is {}".format(self.balance))
    else:
      self.balance -= amount
      time=datetime.now()
      bill = {
        'time':time'
        'bill': amount:
      }
      self.bill.append(bill)
      print("You have paid bill worth {} on ".format(amount,self.get_formatted_time(time))

  def send_money(self,amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter the amount in figures")
      return
    if amount > self.balance:
      print("You don't have enough balance. Your balance is {}".format(self.balance))
    else:
      self.balance -= amount
      time=datetime.now()
      money= {
        'time':time'
        'money': amount:
      }
      self.money.append(money)
      print("You have send money worth {} on ".format(amount,self.get_formatted_time(time))



  def receive_money(self,amount):
    try:
      amount + 1
    except TypeError:
      print("Please enter the amount in figures")
      return
    if amount > self.balance:
      print("You don't have enough balance. Your balance is {}".format(self.balance))
    else:
      self.balance -= amount
      time=datetime.now()
      artime = {
        'time':time'
        'money': amount:
      }
      self.money.append(money)
      print("You have received money worth {} on ".format(amount,self.get_formatted_time(time))
    
 