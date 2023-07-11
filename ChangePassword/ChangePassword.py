from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import configparser
driver = webdriver.Chrome()


def ChnagePW (oldPW ,newPW):
    input_box = driver.find_element(By.ID, "edtOldPassword")
    input_box.send_keys(oldPW)
    input_box = driver.find_element(By.ID, "edtPasswordChange")
    input_box.send_keys(newPW)
    input_box = driver.find_element(By.ID, "edtPasswordChangeConfirm")
    input_box.send_keys(newPW)
    Button_Login = driver.find_element(By.ID, "btnChangeOK")
    Button_Login.click()
    time.sleep(2)
    
def Login (acc ,pw):
    # 打開網頁
    driver.get("https://hrp.hosp.nycu.edu.tw:8082/logon.aspx")
    driver.maximize_window()
    # 找到輸入框元素
    input_box = driver.find_element(By.ID, "edtAccount")
    input_box.send_keys(acc)
    input_box = driver.find_element(By.ID, "edtPassword")
    input_box.send_keys(pw)
    Button_Login = driver.find_element(By.ID, "btnLogon")
    Button_Login.click()
    time.sleep(2)
    Button_Login = driver.find_element(By.ID, "btnPWChange")
    Button_Login.click()
    time.sleep(2)
    

config = configparser.ConfigParser()
config.read('D:\Python\PW.ini')
# get section for account and password
acc = config.get('ACC', 'Account')
pw = config.get('ACC', 'Password')
Newpw = 'KUEkue520'
print("Account:{0} Password:{1} New Password:{2}".format(acc,pw,Newpw))

#edtOldPassword edtPasswordChange edtPasswordChangeConfirm
Login(acc,pw)
ChnagePW(pw,Newpw)
Login(acc,Newpw)
ChnagePW(Newpw,pw)
Login(acc,pw)
time.sleep(5)
#exit()