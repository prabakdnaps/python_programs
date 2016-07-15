import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unidecode
import re
import datetime, time

wd = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd.get(URL)
time.sleep(1)
element=wd.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)
noOfTry=0
filename='noOfTry.html'

def html_create(filename):
	html_page = wd.page_source
	data = html_page.encode('utf-8')
	lines = data.split('"')
	file=open(filename,'w')
	for items in lines:
		file.write(str(items)+'\n')
	file.close()

def noOfTry(filename):
	data_file=open(filename,'r')
	data=data_file.read()
	data_file.close()
	data=data.split('\n')
	total_number=[]
	total_page=[]
	for line in data:
		if '1-100' in line:
			line_data=line.split('>')
			total_number.append(line_data[1][9:18])
	for item in total_number[0]:
		for letter in item:
			if letter!=',':
				total_page.append(letter)
	return int(''.join(total_page))/100
'''while True:
	element=wd.find_element_by_id("ctl00_ucTopTabMenu_lnkCompany")
	element.click()
	time.sleep(15)
	try:
		html_create(filename)
		noOfTry=noOfTry(filename)
	except:
		noOfTry=0
	if noOfTry>0:
		break
print noOfTry'''
a=['C','K','S']
wd1 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd1.get(URL)
time.sleep(1)
element=wd1.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd1.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd2 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd2.get(URL)
time.sleep(1)
element=wd2.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd2.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd3 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd3.get(URL)
time.sleep(1)
element=wd3.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd3.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd4 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd4.get(URL)
time.sleep(1)
element=wd4.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd4.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd5 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd5.get(URL)
time.sleep(1)
element=wd5.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd5.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd6 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd6.get(URL)
time.sleep(1)
element=wd6.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd6.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd7 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd7.get(URL)
time.sleep(1)
element=wd7.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd7.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd8 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd8.get(URL)
time.sleep(1)
element=wd8.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd8.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

wd9 = webdriver.Chrome()
time.sleep(1)
URL='https://sso.construction.com/SingleSignOn/Login.aspx?redirectUrl=http%3a%2f%2fnetwork2.construction.com%2fAuthorizeAccess.aspx%3fReturnUrl%3d%252fHome.aspx'
wd9.get(URL)
time.sleep(1)
element=wd9.find_element_by_name("ctl00$MainContent$txtEmail")
element.send_keys("directofficenow@gmail.com")
element=wd9.find_element_by_name("ctl00$MainContent$txtPassword")
element.send_keys("Direct741")
element.send_keys(Keys.RETURN)

for j in range(40000,50000):
	company_name=[]
	for i in range(100):
		length_no=len(str(i+j*100))
		while length_no<12:
			a.append('0')
			length_no=length_no+1
		a.append(str(i+j*100))
		company_name.append(''.join(a))
		a=['C','K','S']
	mid_url='|'.join(company_name)
	back_url='&FileName=Companies_20160629_'
	back2_url=str(j)+'PM&TemplateFields='
	front_url='http://network2.construction.com/DownloadCSV.aspx?DownloadType=COMPANY&Mode=SINGLE&TemplateId=-1&Items='
	URL1=front_url+mid_url+back_url+back2_url
	index=str(j)
	if index[-1]=='0':
		wd.get(URL1)
	elif index[-1]=='1':
		wd1.get(URL1)
	elif index[-1]=='2':
		wd2.get(URL1)
	elif index[-1]=='3':
		wd3.get(URL1)
	elif index[-1]=='4':
		wd4.get(URL1)
	elif index[-1]=='5':
		wd5.get(URL1)
	elif index[-1]=='6':
		wd6.get(URL1)
	elif index[-1]=='7':
		wd7.get(URL1)
	elif index[-1]=='8':
		wd8.get(URL1)
	else:
		wd9.get(URL1)