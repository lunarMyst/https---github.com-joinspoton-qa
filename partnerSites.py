
# import webdriver and exception handling tools

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException



# choose browser

browser = webdriver.Chrome('/Users/valeriy/Applications/chromedriver')
# browser = webdriver.Safari()
# browser = webdriver.Firefox(executable_path='/Users/valeriy/Downloads/geckodriver')
# browser = webdriver.PhantomJS(executable_path='/Users/valeriy/Desktop/phantomjs-2.1.1-macosx/bin/phantomjs')

# prepare Chrome by deleting old cookies, set url and window size

if browser == webdriver.Chrome:
    browser.set_window_size(1280, 720)

# takes browser to passed in url

def loadPage(URL):
    try:
        browser.get(URL)
        print browser.current_url, " loaded successfully. \n"
    except WebDriverException:
        print URL, " page could not be loaded. \n"
        return False

# scrolls browser to bottom of current page

def scrollToBottom(frame):
    browser.execute_script("return arguments[0].scrollIntoView();", frame)

# find elements within iframe by their classes

def lookForElements():
    try:
        #browser.find_element_by_class_name('tile-background')
        #browser.find_element_by_class_name('event-tile')
        #browser.find_element_by_class_name('header-tile')
        #browser.find_element_by_class_name('tile-background-image')
        #browser.find_element_by_class_name('tile-background-gradient')
        #browser.find_element_by_class_name('menu-button-button')
        #browser.find_element_by_class_name('subscriber-count')
        #browser.find_element_by_class_name('menu-button')
        browser.find_element_by_class_name('add-to-calendar-button')
        print "Stanzacal elements found. \n"

    except NoSuchElementException:
        print "Failed to find stanzacal element(s). \n"
        return None

# tests to see if site has iframe or parent frame stanzacal

def findandswitchtoframe():
    stanzaframe = None
    iframeList = None
    try:
        stanzaParentFrame = browser.find_element_by_class_name('stanzacal')
        stanzaIframe = stanzaParentFrame.find_element_by_tag_name('iframe')
        browser.switch_to.frame(stanzaIframe)
        # print browser.current_url, \
        print "Found stanzacal parent frame. \n"

    except NoSuchElementException:

        # collects all elements with tag 'iframe' and adds them to a list
        try:
            iframeList = browser.find_elements_by_tag_name('iframe')
            # iterates thru list of iframes and looks for one with 'stanza.co' in src attribute

            for i in iframeList:
                source = i.get_attribute('src')
                if "stanza.co" in source:
                    print "Found a Stanza iframe : ", source, "\n"
                    browser.switch_to.frame(i)
                    break

                elif iframeList.index(i) == len(iframeList) - 1 and "stanza.co" not in source:
                    print "Stanza iframe could not be found. \n"

        except NoSuchElementException:
            print browser.current_url, "No iframes could be found. \n"

# main function. Loads url, looks for iframe, switches selenium to it, checks for cal button elements
def testpage(URL):
    if loadPage(URL) == False:
        return None

    findandswitchtoframe()
    lookForElements()

# List of websites to test


testpage('https://arsenal-mania.com/striker-confirms-hes-set-for-arsenal-exit-in-the-coming-weeks/')
testpage('http://www.angelswin-forum.com/forums/forum/11-la-angels-mlb-daily/')

testpage('http://www.49erswebzone.com')
testpage('http://www.allarsenal.com/2017/05/news/player-ratings-gunners-arsenal-v-chelsea/')
testpage('http://www.topix.com/us')
testpage('http://wrestlinginc.com')
testpage('http://www.wowhead.com/forums')

testpage('http://www.sfexaminer.com/')
testpage('https://www.starwarsnewsnet.com/')
testpage('http://www.stltoday.com/sports/')
testpage('http://journalstar.com/sports/huskers/')
testpage('http://www.celticquicknews.co.uk/')

testpage('http://forums.bluemoon-mcfc.co.uk/')
testpage('http://ndnation.com/')
testpage('https://forum.huskermax.com/index.php?forums/football.4/')
testpage('https://tempostorm.com/')
testpage('http://www.toffeeweb.com')

testpage('https://canucksarmy.com/2017/06/01/nation-network-2017-prospect-profiles-36-isaac-ratcliffe/')
testpage('https://www.cityweekly.net')
testpage('https://csgosquad.com/')
testpage('http://csgo-stats.com/')
testpage('negativetest.gg')

