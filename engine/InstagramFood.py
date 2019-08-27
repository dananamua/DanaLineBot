import requests
from bs4 import BeautifulSoup
import json
import csv
#from geopy.distance import geodesic

#前12個食物
def foodSearch(): 
	webContent = requests.get('https://www.instagram.com/howeat219/')
	firstSoup = BeautifulSoup(webContent.text,'html.parser')
	firstdata = firstSoup.findAll('script',{'type':'text/javascript'})[3].text.split('window._sharedData = ')[1]
	firstdata = firstdata[0:len(firstdata)-1]
	count =0
	index = 1
	locationlist = []
	foodTitleInfoList =[]
	replylist =[]
	for time in range(1,13):
		foodAllData = json.loads(firstdata)['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][count]['node']['edge_media_to_caption']['edges'][0]['node']['text']
		foodTitle = foodAllData.split('\n')[0]
		foodFirstInfo = foodAllData.split('🔺')[1]
		foodSecondInfo = foodFirstInfo.split('#')[0]
		temp = [foodTitle,foodSecondInfo]
		foodTitleInfoList.append(temp)
		#bestrecommand = foodAllData.split('✔️')[1]
		#foodbest = bestrecommand.split('-')[0]
		#print(foodAllData)
		reply1 = '{}. {}\n{}\n-----------'.format(index,foodTitle,foodSecondInfo)
		#print(foodbest)
		replylist.append(reply1)

		
		# locationFirstTwlStCall = foodAllData.find('地址：')
		# locationFirstTwlNdCall = foodAllData.find('地點：')
		# if locationFirstTwlNdCall == -1 and locationFirstTwlStCall == -1:
		# 	location = 'no address'
		# else:
		# 	if locationFirstTwlNdCall == -1:
		# 		locationStartIndex = foodAllData.split('地址：')[1]
		# 		location = locationStartIndex.split('\n')[0]
		# 	else:
		# 		locationStartIndex = foodAllData.split('地點：')[1]
		# 		location = locationStartIndex.split('\n')[0]
		# 	#print('地址：{}'.format(locationEndIndex))
		# locationlist.append(location.encode('utf-8').decode('utf-8-sig'))

		count+=1
		index+=1


	#後12個食物

	webcontent1 = requests.get('https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%224029942073%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFCWllJaDlpT0pjVFIzMW1GSVRuRXV1andKdUc1eVAyNVFkXzlRTjlRWlMzUXBWVm5ZQ1E0MjVTRm9yWjN2ei1JMEZ6bHVBZUZUQ19pbmRfcnBuTTNVVw%3D%3D%22%7D').json()
	webcontent2 = requests.get('https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%224029942073%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFCd0NhNktPSXBCNVFtVnRZWlBZV0F6NjBZLV80NnlabDF5V3dCWE5rTmJ5OVZOeEVZNnk0Rmo4cjd0SDJDNFNhNWlmS1FoX1Y5TnRwMUJ3YXR2bjVPVQ%3D%3D%22%7D').json()
	webcontent3 = requests.get('https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%224029942073%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFCTkRmVk16RmNRV3NRdGJqc1ZNUzhTTTFEYmVOeGFnMTEtMTl6N0RFSk1rSGprYnFQZjE0TjRiRUhwSnN0eDlXbk1yUHBpdHhGZzlPRnZmRlpJVENtMA%3D%3D%22%7D').json()
	listContent = list()
	listContent.append(webcontent1)
	listContent.append(webcontent2)
	listContent.append(webcontent3)

	for webcontent in listContent:
		for post in webcontent['data']['user']['edge_owner_to_timeline_media']['edges']:

			url = 'https://www.instagram.com/p/{}'.format(post['node']['shortcode'])
			postContent = requests.get(url)
			soup = BeautifulSoup(postContent.text, 'html.parser')
			##print(soup.select('title')[0].text)
			rawdata = soup.findAll('script',{'type':'text/javascript'})[3].text.split('window._sharedData = ')[1]
			rawdata = rawdata[0:len(rawdata)-1]
			foodalldata = json.loads(rawdata)['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
			foodtitle = foodalldata.split('\n')[0]
			foodfirstinfo = foodalldata.split('🔺')[1]
			foodsecondinfo = foodfirstinfo.split('#')[0]
			temp = [foodtitle,foodsecondinfo]
			foodTitleInfoList.append(temp)
			#bestrecommand = foodAllData.split('✔️')[1]
			#foodbest = bestrecommand.split('-')[0]
			#print(foodalldata)
			reply2='{}. {}\n{}\n-----------'.format(index,foodtitle,foodsecondinfo)
			#print(foodbest)
			replylist.append(reply2)

			
			# locationbackstcall = foodalldata.find('地址：')
			# locationbackndcall = foodalldata.find('地點：')
			# if locationbackstcall == -1 and locationbackndcall == -1:
			# 	location ='no address'
			# else:
			# 	if locationbackndcall == -1:
			# 		locationstartindex = foodalldata.split('地址：')[1]
			# 		location = locationstartindex.split('\n')[0]
			# 	else:
			# 		locationstartindex = foodalldata.split('地點：')[1]
			# 		location = locationstartindex.split('\n')[0]
			# 	#print('地址：{}'.format(locationendindex))
			# locationlist.append(location.encode('utf-8').decode('utf-8-sig'))
			index+=1

	return replylist

#print(foodSearch())
	# print(locationlist)

	
	# userLike =input('請輸入喜歡的食物編號(可複選)(＊注意:編號之間請用一個空格分隔):')
	# if userLike.find(' ') == -1:
	# 	userLikeList =list()
	# 	userLikeList.append(int(userLike))
	# else:
	# 	userLikeList = list(map(int,userLike.split(' ')))

	# likeFoodLocation =[]

	# userLocation = input('輸入您目前的所在位置:')
	# googleMapUser = 'https://www.google.com/maps/search/?api=1&query={}'.format(userLocation)
	# googleContentUser = requests.get(googleMapUser)
	# soupUser = BeautifulSoup(googleContentUser.text,'lxml')
	# coordUser = soupUser.findAll('meta',{'itemprop':'image'})[0]['content'].split('center=')[1].split('&')[0]
	# userLat = coordUser.split('%2C')[0]
	# userLon = coordUser.split('%2C')[1]
	# userlocation = (userLat,userLon)

	# overallList =[]
	# for num in userLikeList:
	# 	googleMapFood = 'https://www.google.com/maps/search/?api=1&query={}'.format(locationlist[num-1])
	# 	googleContentFood = requests.get(googleMapFood)
	# 	soupFood = BeautifulSoup(googleContentFood.text,'lxml')
	# 	coordFood = soupFood.findAll('meta',{'itemprop':'image'})[0]['content'].split('center=')[1].split('&')[0]
	# 	foodLat = coordFood.split('%2C')[0]
	# 	foodLon = coordFood.split('%2C')[1]
	# 	foodLikeLocation = (foodLat,foodLon)
	# 	likeFoodLocation.append(foodLikeLocation)

	# 	distance = geodesic(userlocation,foodLikeLocation).km
	# 	overall = [foodTitleInfoList[num-1], distance]
	# 	overallList.append(overall)
	# overallList.sort(key = lambda x:x[1])
	# index=1
	# print('幫您挑選出最靠近您目前位置的美食:')
	# for info in overallList:
	# 	print('{}.{} \n距離您{}公里'.format(index,info[0],info[1]))
	# 	print('-----------------------')

	

# def combine(section):
# 	smallSoup = BeautifulSoup(htmldoc, 'html.parser')
# 	bodyTag = smallSoup.body
# 	bodyTag.append(section)

# 	return bodyTag


# htmldoc=<!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset="utf-8">
# 		<title> Instagram KH Food</title>
# 	</head>
# 	<body>
# 		<h1></h1>
# 		<p></p>
# 	</body>
# </html>
# '''

# url='https://www.instagram.com/kaohsiung_dacodie/?hl=zh-tw'
# webConnect = requests.get(url)
# webConnect.encoding='UTF-8'
# print(webConnect.text)
# beauSoup = BeautifulSoup(webConnect.text,'html.parser')
# for pic in beauSoup.select('v1Nh3 kIKUG  _bz0w a'):
# 	print('https://www.instagram.com{}'.format(pic['href']))


#browser = webdriver.Chrome('/Users/mac/Desktop/Happy Programmer/Python-turtle/chromedriver')
#browser.get(url)

#browSoup = BeautifulSoup(browser.page_source, 'html.parser')
##description = browSoup.select('.C4VMK span')[0].text
##print(description)
#browser.quit()


'''
config = imgkit.config(wkhtmltoimage='/usr/local/bin/wkhtmltoimage')
imgkit.from_string(str(combine(soup.select('.FyNDV ')[0])),'InstaFood.jpg',config=config)
'''
