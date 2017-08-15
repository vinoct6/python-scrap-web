from selenium import webdriver

# Location of the chromewebdriver
browser = webdriver.Chrome("/Users/p7110429/Desktop/chromedriver/chromedriver")

browser.get("https://google.com")
# Connect to google and execute the script
# browser.execute_script("alert('hello')")

#Take screenshot
browser.save_screenshot("test2.png")
browser.close()
