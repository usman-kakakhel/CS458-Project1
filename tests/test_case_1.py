import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

'''
Test Case 1: Verify that the User is redirected to the Sign up page when clicking on the Sign up now button (1 instance)
'''


base_url = "http://localhost:3000"
sign_in_page = "/signin"
sign_in_xpaths = {'email_input':'/html/body/div/div/div/div/form/input[1]',
		'password_input': '/html/body/div/div/div/div/form/input[2]',
		'sign_in_button': '/html/body/div/div/div/div/form/button',
		'remember_me_checkbox': '/html/body/div/div/div/div/form/div/input',
		'sign_up_link': '/html/body/div/div/div/div/form/a[2]'
		}
		
sign_up_xpaths = {'sign_up_heading': '/html/body/div/div/div/div/h2'}

def test_signup_redirection():
	#initialize headless firefox
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	
	#Load sign in page
	driver.get(base_url + sign_in_page)

	#Verify that the sign in page is loaded by checking sign up link
	delay = 3
	singup_link_element = None
	try:
		singup_link_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_up_link'))))
	except:
		singup_link_element = None
	assert singup_link_element != None
	
	#click sign up link
	singup_link_element.click()
	
	#Verify that the sgin up page is loaded by checking sign up heading.
	singup_heading_element = None
	try:
		singup_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_up_xpaths.get('sign_up_heading'))))
	except:
		singup_heading_element = None
	assert singup_heading_element != None
	driver.close()