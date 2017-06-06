
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# chooses safari as web browser, sends it to a url
driver = webdriver.Safari()
# driver = webdriver.Chrome('/Users/valeriy/Applications/chromedriver')

# river.get('https://stanza.co/@leagueoflegends?embed=true&site=toffeeweb') # 'http://local.spoton.it/@leagueoflegends?embed=true&site=toffeeweb')
print driver.get_window_size()
driver.maximize_window()
print driver.get_window_size()
element = driver.page_source
print (driver.current_url)

driver.set_window_size(1280, 720)

# open category menu
menuButton = driver.find_element_by_class_name('menu-button-button')
menuButton.click()

# find top line "choose a category"
chooseCategory = driver.find_element_by_class_name('tiny-menu-header')

# find buttons category menu
allButtonCategoryMenu = driver.find_element_by_class_name('tiny-menu-category')
allButtonCategoryMenu.click()

# close category menu
closeMenuButton = driver.find_element_by_class_name('tiny-menu-close')
# closeMenuButton.click()

# check presence of elements
listOfCategories = driver.find_element_by_class_name('tile-list')
listOfCategories.click()

driver.find_element_by_class_name('subscriber-count')
driver.find_element_by_class_name('grid-header-logo')
driver.find_element_by_class_name('grid-header')

# assert text on page
assert "League of Legends" in driver.page_source
# assert "Subscribers" in driver.page_source
assert "Category" in driver.page_source
assert expected_conditions.new_window_is_opened

# collect random info
print (driver.get_window_size())
print (driver.current_url)

# find ad tile
driver.find_elements_by_name('GoogleActiveViewClass')
driver.find_elements_by_name('League of Legends')
driver.find_element_by_id('538915532-container')

# find stanza logo
stanzaButton = driver.find_element_by_class_name('grid-header-logo')

# find and click 'add to calendar' button
addToCalendarButton = driver.find_element_by_class_name('add-to-calendar-button')
addToCalendarButton.click()
driver.switch_to.default_content()

# close browser
driver.close()






