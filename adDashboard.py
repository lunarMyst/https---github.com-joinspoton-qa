
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('/Users/valeriy/Applications/chromedriver')
browser.set_window_size(1280, 720)

URL = 'http://stanza.dance/publisher'
browser.get(URL)

browser.implicitly_wait(5)

forgotPasswordButton = browser.find_element_by_class_name('Linkify')
forgotPasswordButton.click()

resetPasswordHeader = browser.find_element_by_class_name('Linkify')
assert resetPasswordHeader.text == 'RESET YOUR PASSWORD'

forgotPasswordEmailField = browser.find_element_by_css_selector('#root > div > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div > div:nth-child(2) > input[type="text"]')
forgotPasswordEmailField.send_keys('wrongformat')
forgotPasswordEmailField.send_keys(Keys.RETURN)

cancelButton = browser.find_element_by_css_selector('#root > div > div > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > p > span > span')
cancelButton.click()

emailField = browser.find_element_by_css_selector('#root > div > div > div > div > div.rmq-f23967a6.rmq-30c1d30d > div:nth-child(1) > div > div:nth-child(2) > input[type="text"]')
emailField.send_keys('demo-u@stanza.co')
emailField.send_keys(Keys.RETURN)

passwordField = browser.find_element_by_css_selector('#root > div > div > div > div > div.rmq-f23967a6.rmq-30c1d30d > div:nth-child(2) > div > div:nth-child(2) > input[type="password"]')
passwordField.send_keys('godemo')
emailField.send_keys(Keys.RETURN)

signInButton = browser.find_element_by_css_selector('#root > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button > p')
signInButton.send_keys(Keys.RETURN)
# signInButton.click()




