from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

Chrome_profile_path = "user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Wtsp"


options = webdriver.ChromeOptions()
options.add_argument(Chrome_profile_path)

driver = webdriver.Chrome(executable_path = "C:\chromedriver\chromedriver", options=options)

driver.get('https://web.whatsapp.com/')
groups = ['Tanishq']
message = ['Dekho','Ye to automate','ho gaya']

for group in groups:
    search_box_path = '/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]'
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, search_box_path))
    )
    search_box.clear()
    time.sleep(2)

    search_box.send_keys(group)
    time.sleep(2)
# //*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span
    grp_name = driver.find_element_by_xpath("//span[@title='"+group+"']")
    # print(grp_name)
    grp_name.click()

    time.sleep(2)

    input_box = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
    for i in message:
        input_box.send_keys(i)
        input_box.send_keys(Keys.ENTER)
        time.sleep(0.5)