from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Edge open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

# driver.get("https://www.amazon.com/SAMSUNG-SmartTag2-Bluetooth-Tracker-Tracking/dp/B0CCBXRYRC/?_encoding"
#            "=UTF8&pd_rd_w=5FAE7&content-id=amzn1.sym.034d21de-f825-413a-8c94-7d57d209901e&pf_rd_p"
#            "=034d21de-f825-413a-8c94-7d57d209901e&th=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
#
# print(f'The Price is {price_dollar}.{price_cents}')

# close current tab
# driver.close()
# close browser
# driver.quit()

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

driver.quit()
