from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Keep Edge open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
