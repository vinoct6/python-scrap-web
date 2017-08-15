def flatten_list(lst):
    return [item for sublist in lst for item in sublist]


from selenium import webdriver

browser = webdriver.Chrome("/Users/p7110429/Desktop/chromedriver/chromedriver")
browser.get("https://www.reddit.com/r/india/")

titles = []

# Extract outbound links from first 3 pages
for i in range(1, 3):
    elements = browser.find_elements_by_css_selector("a.title.may-blank.outbound")
    titles.append([e.text for e in elements])
    next_button = browser.find_element_by_css_selector(".next-button a")
    next_button.click()

print(flatten_list(titles))

browser.close()
