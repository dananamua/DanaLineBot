import twder

def currencySearch(search):
	if search == '美金':
		DollarList = twder.now('USD')
		reply = '{}\n{}美金的極其賣出價:{}'.format(DollarList[0],search,DollarList[4])
		return reply