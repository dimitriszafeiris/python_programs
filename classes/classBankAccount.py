class Account():
	
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self,d_amount):
		self.balance = self.balance + d_amount
		print (f"You have added {d_amount} to your bank account.")

	def withdrawal(self,w_amount):

		if self.balance >= w_amount:
			self.balance = self.balance - w_amount
			print ("Withdrawal is accepted.")
		else:
			print ("Sorry, you don't have enough funds.")

	def __str__(self):
		return f"Owner: {self.owner} \nBalance: {self.balance}"