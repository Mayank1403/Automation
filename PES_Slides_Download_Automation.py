"""
	Pre-requisites:
	selenium needs to be installed (pip install selenium)
	Firefox
	Firefox should be configured to download/save PDF by default.
	geckodriver
	Things that have to be changed in this file:
	Insert your SRN in between the double quotes equated to the username variable
	Insert your password in between the double quotes equated to the password variable
	Insert path to the firefox profile you configured. (Note: A firefox profile with the pre-requisites has to be made in order for the script to run properly)
	Run as follows:
	python download.py <position_of_course_in_list> <starting_lecture_number> <ending_lecture_number>
	example:
	python download.py 3 5 12 1
	Running the above code downloads lectures 5-12(both inclusive) of the 3rd course in 'My Courses' list
"""

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def download(args):
	link = "https://pesuacademy.com/Academy/"
	username = "username"
	password = "password"

	firefox_options = Options()
	firefox_options.add_argument('--headless')
	driver = webdriver.Firefox(executable_path=r'C:\Users\DELL\AppData\Roaming\npm\node_modules\geckodriver\geckodriver.exe',firefox_profile='C:\\Users\\DELL\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\v8jui852.default-release',options=firefox_options)

	driver.get(link)
	un = driver.find_element_by_id('j_scriptusername')
	un.send_keys(username)
	pw = driver.find_element_by_name('j_password')
	pw.send_keys(password)
	driver.find_element_by_id('postloginform#/Academy/j_spring_security_check').click()

#/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr[1]/td[4]
#/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/a
#/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr[1]/td[1]
#/html/body/div[3]/div[2]/div/div[2]/ul/li[3]/a
#/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr[10]/td[1]
#/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/a
#/html/body/div[3]/div[2]/div/div[2]/ul/li[3]/a

	for i in range(int(args[2]),int(args[3])+1):
		time.sleep(2)
		driver.find_element_by_id('menuTab_653').click()																							# Click 'My courses'
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div/div/table/tbody/tr[4]/td[2]').click()		# Click course name
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/ul/li[3]/a').click()						# Click unit number
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr[' + str(i) +']/td[1]').click()					# Click lecture number
		#driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/table/tbody/tr[1]/td[1]').click()					# Click lecture number
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[3]/a').click()														# Click 'slides' tab
		
if __name__ == "__main__":
	download(sys.argv)