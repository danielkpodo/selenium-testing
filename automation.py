from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
test_url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
browser.maximize_window()  # you can resize with media queries

browser.get(test_url)

# assert "Selenium Easy Demo" in browser.title test if a word exists in title

# Utilizing Selectors - refer to [http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/]
show_message_button = browser.find_element_by_class_name('btn-default')
# btn_text = button.get_attribute('innerHTML')
# print(btn_text)

assert "Show Message" in browser.page_source

user_message = browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Daniel Narh is a prolific programmer! ')
show_message_button.click()


# Closing the browser
# browser.close -> closes the current browser
# browser.quit -> quits the entire driver

browser.close()
