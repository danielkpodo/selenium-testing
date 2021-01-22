from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
test_url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
browser.maximize_window()  # you can resize with media queries

browser.get(test_url)

# assert "Selenium Easy Demo" in browser.title test if a word exists in title

# Utilizing Selectors
button = browser.find_element_by_class_name('btn-default')
btn_text = button.get_attribute('innerHTML')
print(btn_text);
