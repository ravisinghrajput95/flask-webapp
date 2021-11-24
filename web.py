from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window() 

driver.get("http://192.168.1.5:5000/edit")
time.sleep(4)
assert "Todo" in driver.title

task=driver.find_element_by_xpath("//input[@type='text'][@name='title']")
task.send_keys('Test')

add=driver.find_element_by_xpath("//button[@class='ui blue button'][@type='submit']")
add.click()
time.sleep(4)

update=driver.find_element_by_xpath('/html/body/div/div/a[1]')
update.click()
time.sleep(4)

delete=driver.find_element_by_xpath('/html/body/div/div/a[2]')
delete.click()
time.sleep(4)

driver.close()  
