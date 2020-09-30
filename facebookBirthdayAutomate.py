#selenium is module used for web automation

# C:\\Users\\anki0\\Desktop

from selenium import webdriver
browser = webdriver.Chrome('C:\\Users\\anki0\\Desktop\\chromedriver.exe')
browser.get('https:\\www.facebook.com')

user_id = input("Enter the username: ")
password = input("Enter the password: ")

# print(user_id)
# print(password)

ep = browser.find_element_by_id("email")
ep.send_keys(user_id)
ps = browser.find_element_by_id("pass") 
ps.send_keys(password)
login = browser.find_element_by_id("u_0_b")
login.click()

k = '//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]'
n= browser.find_element_by_xpath(k).get_attribute('textContent')
num=n[0]
num=int(num)
print(num)
# browser.quita