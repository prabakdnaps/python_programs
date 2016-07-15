from os import listdir
from os.path import isfile, join
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
element=wd.find_element_by_id("ctl00_ucTopTabMenu_lnkProjects")
element.click()
time.sleep(5)
working_dir='D://auto//dodge//projects'
onlyfiles=[f for f in listdir(working_dir) if isfile(join(working_dir,f))]
files_to_join=[]

for file in onlyfiles:
	if 'Projects' in file:
		files_to_join.append(file)


for i in range(len(files_to_join)):
	offset=10
	project_no=[]
	ver_no=[]
	data_file=open(working_dir+'//'+files_to_join[i+offset],'r')
	data=data_file.read()
	data_file.close()
	data=data.split('\n')
	for items in data[1:]:
		line_data=items.split(',')
		if len(line_data)>2:
			project_no.append(line_data[0][1:-1])
			ver_no.append(line_data[1])
	project_noStr='|'.join(project_no)
	ver_no_Str='|'.join(ver_no)
	element=wd.find_element_by_id("ctl00_ucTopTabMenu_lnkProjects")
	element.click()
	time.sleep(3)
	wd.execute_script('addSelectedProjectsToSession(\"'+project_noStr+'\",\"'+ver_no_Str+'\");')
	time.sleep(2)
	wd.execute_script('window.open(\'DownloadFirms.aspx\', \'_parent\', \'height=150px,width=400px,status=0,resizable=0,scrollbars=0,center=1,location=0,menubar=0\');')
	time.sleep(2)
	element=wd.find_element_by_id("ctl00_ucTopTabMenu_lnkProjects")
	element.send_keys(Keys.ESCAPE)
	time.sleep(1)
	print i+offset

