import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

'''
Test Case 3: Verify that Enter key works as a substitute for the Sign-in button 
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
passwords = ['a', 'aaaa', 'a'*60, 'a'*61, 'a'*7, 'a'*24, 'UTQUMax5sgeY8U8']

def test_enter_key_range_short():
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
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
	assert alert_range_element != None
	expected_alert_texts = ['Your password must contain between 4 and 60 characters!']
	assert alert_range_element.text in expected_alert_texts
	alert_range_element.accept()
	driver.close()
	
def test_enter_key_range_lower_edge():
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
	
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	homepage_heading_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
		try:
			homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
		except:
			homepage_heading_element = None


	expected_alert_texts = ['Password is wrong!','No such user!']
	assert (alert_range_element != None) or (homepage_heading_element != None)
	if alert_range_element != None:
		assert alert_range_element.text in expected_alert_texts
		alert_range_element.accept()
	driver.close()
	
def test_enter_key_range_upper_edge():
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
	password_input_element.send_keys(passwords[2])
	
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	homepage_heading_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
		try:
			homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
		except:
			homepage_heading_element = None


	expected_alert_texts = ['Password is wrong!','No such user!']
	assert (alert_range_element != None) or (homepage_heading_element != None)
	if alert_range_element != None:
		assert alert_range_element.text in expected_alert_texts
		alert_range_element.accept()
	driver.close()
	
def test_enter_key_range_long():
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
	password_input_element.send_keys(passwords[3])
	
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
	assert alert_range_element != None
	expected_alert_texts = ['Your password must contain between 4 and 60 characters!']
	assert alert_range_element.text in expected_alert_texts
	alert_range_element.accept()
	driver.close()
	
def test_enter_key_range_valid_1():
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
	password_input_element.send_keys(passwords[4])
	
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	homepage_heading_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
		try:
			homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
		except:
			homepage_heading_element = None


	expected_alert_texts = ['Password is wrong!','No such user!']
	assert (alert_range_element != None) or (homepage_heading_element != None)
	if alert_range_element != None:
		assert alert_range_element.text in expected_alert_texts
		alert_range_element.accept()
	driver.close()
	
def test_enter_key_range_valid_2():
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
	password_input_element.send_keys(passwords[5])
	
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	homepage_heading_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
		try:
			homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
		except:
			homepage_heading_element = None


	expected_alert_texts = ['Password is wrong!','No such user!']
	assert (alert_range_element != None) or (homepage_heading_element != None)
	if alert_range_element != None:
		assert alert_range_element.text in expected_alert_texts
		alert_range_element.accept()
	driver.close()
	
def test_enter_key_range_valid_3():
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
	password_input_element.send_keys(passwords[6])
	
	password_input_element.send_keys(Keys.ENTER)
	
	alert_range_element = None
	homepage_heading_element = None
	try:
		alert_range_element = WebDriverWait(driver, delay).until(EC.alert_is_present())
	except:
		alert_range_element = None
		try:
			homepage_heading_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('homepage_heading'))))
		except:
			homepage_heading_element = None


	expected_alert_texts = ['Password is wrong!','No such user!']
	assert (alert_range_element != None) or (homepage_heading_element != None)
	if alert_range_element != None:
		assert alert_range_element.text in expected_alert_texts
		alert_range_element.accept()
	driver.close()