from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)
Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim. getBalance()
Jim.deposit(100)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()
Blaze.deposit(100)
Blaze.getBalance()
Blaze.transfer(500, Sara)
Blaze.getBalance()
Blaze.withdraw(50)
Blaze.getBalance()
