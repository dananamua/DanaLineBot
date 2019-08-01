import twder

def currencySearch(search):
	DollarList = twder.now_all()[search]
	reply = '{}\n{}的極其賣出價:{}'.format(DollarList[0],search,DollarList[4])
	return reply