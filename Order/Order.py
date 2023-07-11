from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import configparser


config = configparser.ConfigParser()
config.read('D:\Python\PW.ini')
# get section for account and password
acc = config.get('ACC', 'Account')
pw = config.get('ACC', 'Password')
print("Account:{0} Password:{1}".format(acc,pw))
#exit()


# 使用Chrome瀏覽器
driver = webdriver.Chrome()
# 打開網頁
driver.get("http://hisupdatea.ymuh.ym.edu.tw/MealOrder/Login")
driver.maximize_window()
# 找到輸入框元素
input_box = driver.find_element(By.ID, "ContentPlaceHolder1_MemberLogin1_TextBox_Account")
input_box.send_keys(acc)
input_box = driver.find_element(By.ID, "ContentPlaceHolder1_MemberLogin1_TextBox_Password")
input_box.send_keys(pw)
Button_Login = driver.find_element(By.ID, "ContentPlaceHolder1_MemberLogin1_LoginBtn")
Button_Login.click()
Button_Login = driver.find_element(By.ID, "ContentPlaceHolder1_MemberLogin1_ButtonAgreee")
Button_Login.click()
#

# 關閉瀏覽器
input("點餐系統開啟...")
#driver.quit()