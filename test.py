#Author: Imad Kalboneh
#Date created: June 25, 2017
#Last updated; January 10, 2019

import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = 'michaelsfirm.ca'

#infinite loop
while(True):
	t = time.clock()

	#make sure site can load
	response = subprocess.Popen(["ping", site, "-n", '1'], stdout=subprocess.PIPE).stdout.read()

	if response != -1: 
		#open up chrome window and load the site
		driver = webdriver.Chrome()
		driver.get("http://www." + site)

		#find parameter names and fill them
		f_name = driver.find_element_by_name('input_1.3')
		f_name.send_keys('first name test')

		l_name = driver.find_element_by_name('input_1.6')
		l_name.send_keys('last name test')

		email = driver.find_element_by_name('input_2')
		email.send_keys('imad_kalboneh@hotmail.com')

		phone = driver.find_element_by_name('input_3')
		phone.send_keys('9999999999')

		case_details = driver.find_element_by_name('input_4')
		case_details.send_keys('case detail test')

		#driver.find_element_by_xpath("//input[@type='submit' and @value='SEND']").click()
		time.sleep(3) #wait 3 seconds for the form to submit
		driver.close()
		
		#sleeps for 24 hours before running again		
		#(3600 seconds * 24) - time to run the program since enteringg while statement
		#the above makes sure process time is subtracted to amke sure
		#it runs at the same time daily
		time.sleep((3600 * 24) - (time.clock() - t))
			
	else:
		print('site not found')