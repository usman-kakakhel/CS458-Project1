import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

'''
Test Case 4: Verify that the User is able to Login with Valid Credentials 
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
homepage_xpaths = {'homepage_heading': '/html/body/div/div/div/div/h2'}
emails = ['a@b.com', 'a@b2.com', 'msaboor35@gmail.com']
passwords = ['aaab', 'UTQUMax5sgeY8U8', 'a'*7, 'a'*24]

def test_login_valid_1():
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(base_url + sign_in_page)

	delay = 3
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None
	
	
	email_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('email_input'))
	email_input_element.clear()
	email_input_element.send_keys(emails[0])
	password_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('password_input'))
	password_input_element.clear()
	password_input_element.send_keys(passwords[0])
	
	sign_in_button_element.click()
	
	homepage_heading_element = None
	try:
		homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
	except:
		homepage_heading_element = None
	assert (homepage_heading_element != None)
	driver.close()

def test_login_valid_2():
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(base_url + sign_in_page)

	delay = 3
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None
	
	
	email_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('email_input'))
	email_input_element.clear()
	email_input_element.send_keys(emails[2])
	password_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('password_input'))
	password_input_element.clear()
	password_input_element.send_keys(passwords[1])
	
	sign_in_button_element.click()
	
	homepage_heading_element = None
	try:
		homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
	except:
		homepage_heading_element = None
	assert (homepage_heading_element != None)
	driver.close()	
	
def test_login_invalid_1():
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(base_url + sign_in_page)

	delay = 3
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None
	
	
	email_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('email_input'))
	email_input_element.clear()
	email_input_element.send_keys(emails[0])
	password_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('password_input'))
	password_input_element.clear()
	password_input_element.send_keys(passwords[1])
	
	sign_in_button_element.click()
	
	alert_range_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None

	expected_alert_texts = ['Password is wrong!']
	assert alert_range_element != None
	assert alert_range_element.text in expected_alert_texts
	alert_range_element.accept()
	driver.close()
	
def test_login_invalid_2():
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(base_url + sign_in_page)

	delay = 3
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None
	
	
	email_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('email_input'))
	email_input_element.clear()
	email_input_element.send_keys(emails[2])
	password_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('password_input'))
	password_input_element.clear()
	password_input_element.send_keys(passwords[2])
	
	sign_in_button_element.click()
	
	alert_range_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None

	expected_alert_texts = ['Password is wrong!']
	assert alert_range_element != None
	assert alert_range_element.text in expected_alert_texts
	alert_range_element.accept()
	driver.close()
	
def test_login_invalid_3():
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(base_url + sign_in_page)

	delay = 3
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None
	
	
	email_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('email_input'))
	email_input_element.clear()
	email_input_element.send_keys(emails[1])
	password_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('password_input'))
	password_input_element.clear()
	password_input_element.send_keys(passwords[1])
	
	sign_in_button_element.click()
	
	alert_range_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None

	expected_alert_texts = ['No such user!']
	assert alert_range_element != None
	assert alert_range_element.text in expected_alert_texts
	alert_range_element.accept()
	driver.close()

def test_login_invalid_4():
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(base_url + sign_in_page)

	delay = 3
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None
	
	
	email_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('email_input'))
	email_input_element.clear()
	email_input_element.send_keys(emails[1])
	password_input_element = driver.find_element_by_xpath(sign_in_xpaths.get('password_input'))
	password_input_element.clear()
	password_input_element.send_keys(passwords[3])
	
	sign_in_button_element.click()
	
	alert_range_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None

	expected_alert_texts = ['No such user!']
	assert alert_range_element != None
	assert alert_range_element.text in expected_alert_texts
	alert_range_element.accept()
	driver.close()