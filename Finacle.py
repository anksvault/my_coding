#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : Finacle.py                                                #
# Py Versions : 2.7, 3.5+                                                 #
# Description : Demonstration of Class, OOPs, Error Handling in Python    #
# Execute     : python Finacle.py                                         #
#=========================================================================#

class Bank:
    cust_id=0
    cust_names = {'dummy':[0,0]}

    def __init__(self):
        print("========================= FINACLE =========================")

    def add_cust(self,name,dep=0):
        Bank.cust_id += 1
        Bank.cust_names[name] = [Bank.cust_id,dep]
        print("\nThe Following Cust is added: {}".format(Bank.cust_names[name]))

    def deposits(self,name,depamt):
        Bank.cust_names[name][1] = Bank.cust_names[name][1] + depamt
        print("\nChanges Adjusted. Current Balance: {}".format(Bank.cust_names[name][1]))

    def withdraw(self,name,witamt):
        Bank.cust_names[name][1] = Bank.cust_names[name][1] - witamt
        print(f"\nChanges Adjusted. Current Balance: {Bank.cust_names[name][1]}")

    def findcust(self,name):
        if name == 'ALL':
            print("Following are the customer details in the records: \n")
            for record in Bank.cust_names.keys():
                print(f"\nCustomerName: {record}\nCustomerID: {Bank.cust_names[record][0]}\nBalance: {Bank.cust_names[record][1]}\n")
            
        elif name in Bank.cust_names.keys():
            print(f"\nSearch Results:\nCustomer Name: {name}\nCustomer_ID: {Bank.cust_names[name][0]}\nCustomer Acc. Bal: {Bank.cust_names[name][1]}")
        else:
            print("\nCustomer not found in the records")

    def __str__(self):
        return "Author: Ankit Vashisth\nModule Version: 0.3\nDescription:Banking System"

## Initialization.
mybank = Bank()
print(mybank)

## Flag to kill infine loop.
exitflag = 0

## Loops until user confirmation for exit code.
while exitflag == 0:
	## Try Catch block for initial user input.
	try:
		userinput = int(input("Please enter the instruction:\n1.Add Customer\n2.Deposits\n3.Withdrawal\n4.Find Customer\n5.Quit\nYour Instruction: "))
		
	except:
		print("\nInvalid Entry. Please enter integer value from 1 to 5")
		
	else:
		if userinput in [1,2,3,4,5]:

			if userinput == 1:
				try:
					addcinp = int(input("\nPlease enter your choice:\n1.Add Customer with Deposit\n2.Add Customer without Deposit:\nYour Instruction: "))
					
				except:
					print("\nInvalid Entry. Please enter integer value which should be either 1 or 2.")
					
				else:
					if addcinp == 1 or addcinp == 2:

						if addcinp == 1:
							try:
								cname = input("\nCustomer Name: ")
								cdep = int(input("Initial Deposit Amount: "))

							except:
								print("Invalid Value! Please enter Numeric Value for Deposit Amount")

							else:
								## Add Customer with Deposits.
								mybank.add_cust(cname,cdep)
					
						elif addcinp == 2:
							cname = input("\nCustomer Name: ")
							## Add Customer without Deposits.
							mybank.add_cust(cname)

						else:
							print("\nInvalid Choice!")

			elif userinput == 2:
				## Deposits
				cname = input("Please enter Customer Name: ")

				try:
					depamt = int(input("Please Enter Deposit Amount: "))
				
				except:
					print("\nException! Please enter numeric value for the customer amount.")

				else:
					if cname in Bank.cust_names.keys():
						mybank.deposits(cname,depamt)

					else:
						print("\nERROR! Customer name doesn't exist in the records")

			elif userinput == 3:

				try:
					cname = input("\nPlease enter Customer Name: ")
					wamt = int(input("Please enter the withdrawal amount: "))

				except:
					print("\nInput Exception. Please enter numeric value for withdrawal amount.")

				else:
					## Withdrawal
					if cname in Bank.cust_names.keys():
						if wamt > Bank.cust_names[cname][1]:
							print(f"\nWithdrawal Amount is greater than Current Balance {Bank.cust_names[cname][1]}")

						else:
							mybank.withdraw(cname,wamt)

					else:
						print("\nERROR! Customer name doesn't exist in the records")

			elif userinput == 4:
				cname=input("\nPlease enter the name of the customer whose records needs to be fetched [ALL for All Cust Data]: ")
				mybank.findcust(cname)

			elif userinput == 5:
				print("\nExit Code Introduced!")
				exitflag = 1
		else:
			print("\nInvalid Choice! Please re-enter the instruction code.")

