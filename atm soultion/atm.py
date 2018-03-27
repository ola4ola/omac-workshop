# allowed papers: 100, 50, 10, 5, and rest of request
valid_currency = [100, 50, 10, 5]

class ATM:
	def __init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name
	def withdraw (self, request):
		print 'Welcome to' + self.bank_name
		print 'current balance =' + str(self.balance)
		print '==========================='
		
		if request > self.balance:
			print 'no enough balance'
			print '======================='
			return 0
		elif request <= 0 :
			print ' you should enter a request more than zero'
			return 0
		
		remain = self.balance - request
		for currency in valid_currency:
			while request >= currency:
				print 'give ' + str(currency)
				request -= currency
		if request > 0:
			print 'give ' + str(request)
		print'==================================='
		return remain

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)



