from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import configparser


config = configparser.ConfigParser()
config.read('D:\Python\PW.ini')
# get section for account and password
acc = config.get('ACC', 'Account')
pw = config.get('ACC', 'Password')
print("Account:{0} Password:{1}".format(acc,pw))
#exit()

#driver.quit()
def confirm(prompt):
    while True:
        response = input(prompt + " (yes/no): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("請輸入 'yes' 或 'no'.")


def CheckInOut(PunchInOut):
    # 使用Chrome瀏覽器
    driver = webdriver.Chrome()
    # 打開網頁
    driver.get("https://hrp.hosp.nycu.edu.tw:8082/logon.aspx")
    driver.maximize_window()
    # 找到輸入框元素
    input_box = driver.find_element(By.ID, "edtAccount")
    input_box.send_keys(acc)
    input_box = driver.find_element(By.ID, "edtPassword")
    input_box.send_keys(pw)
    if PunchInOut == '1':
        #btnDutyIn    
        Button_Login = driver.find_element(By.ID, "btnDutyIn")
    else:
        #btnDutyOut
        Button_Login = driver.find_element(By.ID, "btnDutyOut")
    Button_Login.click()
    print("打卡完成")
    time.sleep(6)

    
    

# 確認參數數量
if len(sys.argv) < 2:
    print("請提供參數")
    sys.exit(1)
# 取得參數值
PunchInOut = sys.argv[1]
result = "上班打卡" if PunchInOut == "1" else "下班打卡"
if confirm("目前為{}確定要繼續嗎?(Y/N)".format(result)):
    CheckInOut(PunchInOut)
else:
    print("取消打卡")
    

    