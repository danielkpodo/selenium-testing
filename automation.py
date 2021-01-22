from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
test_url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
browser.maximize_window()  # you can resize with media queries

browser.get(test_url)

assert "Selenium Easy Demo" in browser.title


# 