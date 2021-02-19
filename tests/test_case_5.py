import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import os
import shutil

'''
Test Case 5: Verify that user has to login again after logging out.
'''

base_url = "http://localhost:3000"
sign_in_page = "/signin"
profile_page = "/profile"
sign_in_xpaths = {'email_input':'/html/body/div/div/div/div/form/input[1]',
		'password_input': '/html/body/div/div/div/div/form/input[2]',
		'sign_in_button': '/html/body/div/div/div/div/form/button',
		'remember_me_checkbox': '/html/body/div/div/div/div/form/div/input',
		'sign_up_link': '/html/body/div/div/div/div/form/a[2]'
		}
		
sign_up_xpaths = {'sign_up_heading': '/html/body/div/div/div/div/h2'}
homepage_xpaths = {'homepage_heading': '/html/body/div/div/div/div/h2',
					'sign_out_button': '/html/body/div/div/div/div/button'
					}
emails = ['msaboor35@gmail.com']
passwords = ['UTQUMax5sgeY8U8']

def test_session():
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



	sign_out_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, homepage_xpaths.get('sign_out_button'))))
	sign_out_button_element.click()
	
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None


	driver.get(base_url + profile_page)
	sign_in_button_element = None
	try:
		sign_in_button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, sign_in_xpaths.get('sign_in_button'))))
		
	except:
		sign_in_button_element = None
	assert sign_in_button_element != None