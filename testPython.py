
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get('https://www.stanza.co')

assert "personalize your calendar"
assert 'Search for StanzaCals to sync or embed'
assert 'Don\'t let your fans miss a moment'

hamburgerButton = driver.find_element_by_class_name('icon-hamburger')
hamburgerButton.click()

aboutUsButton = driver.find_elements_by_css_selector('AboutUs')
joinUsButton = driver.find_elements_by_css_selector('Join Us')

closeIcon = driver.find_element_by_class_name('icon-close-1')
closeIcon.click()

signInButton = driver.find_element_by_class_name('normal')
signInButton.click()

allGamesButton = driver.find_element_by_class_name('category third-second-transition ng-binding')
allGamesButton.click()






