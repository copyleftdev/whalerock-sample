from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://www.whalerockindustries.com/")
driver.find_element(By.linkText("View Profile")).click()
