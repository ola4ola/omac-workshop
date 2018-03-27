# allowed papers: 100, 50, 10, 5, and rest of request

balance = 500

valid_currency = [100, 50, 10, 5]

def withdraw (balance, request):
	print 'current balance =' + str(balance)
	
	if request > balance:
		print 'no enough balance'
		return 0
	elif request <= 0 :
		print ' you should enter a request more than zero'
		return 0
	
	remain = balance - request
	for currency in valid_currency:
		while request >= currency:
			print 'give' + str(currency)
			request -= currency
	if request > 0:
		print 'give' + str(request)
	return remain

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
