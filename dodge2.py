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
time.sleep(3)
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


element=wd.find_element_by_id("ctl00_ucTopTabMenu_lnkProjects")
element.click()
time.sleep(5)

noOfTry=1537
while noOfTry>0:
	time.sleep(2)
	element=wd.find_element_by_id("project-select-all")
	element.click()
	time.sleep(2)
	element.send_keys(Keys.ESCAPE)
	time.sleep(1)
	element=wd.find_element_by_id("btnProjectActions")
	element.click()
	time.sleep(2)
	element=wd.find_element_by_id("ctl00_contentPlaceHolderHeader_Actions_liSaveProjects")
	element.click()
	time.sleep(2)
	element=wd.find_element_by_id("rbCSV")
	element.click()
	time.sleep(1)
	element=wd.find_element_by_id("downloadProjectSubmit")
	element.click()
	time.sleep(1)
	element=wd.find_element_by_id("ctl00_contentPlaceHolderHeader_ProjectResult_pagerTop_Next")
	element.click()
	time.sleep(1)
	noOfTry=noOfTry-1

	

