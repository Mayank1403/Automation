
# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
  
# open Chrome
driver = webdriver.Firefox(executable_path=
    r'C:\Users\DELL\AppData\Roaming\npm\node_modules\geckodriver\geckodriver.exe',firefox_profile='C:\\Users\\DELL\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\v8jui852.default-release')
  
# # Open URL
# driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeqPpV4uVey9u81aBa1Eh6kjtD8vsAQlmtS3kBVi7WRTSGiMA/viewform')
  
# # wait for one second, until page gets fully loaded
# time.sleep(1)
  
# Data
datas = [
    ["2","1","2","1","2","1","1","4","3"],
    ["2","1","2","1","1","2","1","5","3"],
    ["2","2","2","4","2","2","2","3","3"],
    ["2","1","3","4","2","1","1","2","3"],
    ["2","3","2","4","2","3","3","2","3"],
    ["2","1","1","1","4","3","1","2","3"],
    ["2","4","4","1","2","2","4","2","3"],
    ["2","2","2","1","2","1","2","2","3"],
    ["2","3","3","1","2","1","3","2","1"],
    ["2","1","1","1","2","4","1","5","1"],
    ["2","1","3","1","2","2","1","5","1"],
    ["2","2","4","1","3","2","2","5","1"],
    ["2","3","1","1","2","1","3","5","1"],
    ["2","4","2","4","2","3","4","5","1"],
    ["2","1","3","1","2","1","1","5","1"],
    ["2","1","4","1","2","3","1","1","1"],
    ["2","2","2","1","2","3","2","1","5"],
    ["2","2","3","4","4","1","2","1","2"],
    ["2","2","3","4","2","4","2","1","2"],
    ["2","3","3","4","2","2","3","1","2"],
    ["2","4","2","4","2","2","4","1","1"],
    ["2","4","2","1","1","2","4","3","2"],
    ["1","4","2","1","2","1","4","3","5"],
    ["2","1","2","1","2","3","1","4","3"],
    ["2","1","2","1","1","3","1","5","3"],
    ["2","2","2","4","2","3","2","3","3"],
    ["2","1","3","4","3","1","1","2","3"],
    ["2","3","2","4","2","2","3","2","3"],
    ["2","1","1","1","2","3","1","2","3"],
    ["2","4","4","1","2","2","4","2","3"],
    ["2","2","2","1","2","1","2","2","3"],
    ["2","3","3","1","5","2","3","2","1"],
    ["2","1","1","1","1","4","1","5","1"],
    ["2","1","3","1","2","2","1","5","1"],
    ["2","2","4","1","2","2","2","5","1"],
    ["2","3","1","1","2","1","3","5","1"],
    ["2","4","2","4","3","3","4","5","1"],
    ["2","1","3","1","1","1","1","5","1"],
    ["2","1","4","1","2","3","1","1","1"],
    ["2","2","2","1","1","3","2","1","5"],
    ["2","2","3","4","2","1","2","1","2"],
    ["2","2","3","4","2","4","2","1","2"],
    ["2","3","3","4","1","1","3","1","2"],
    ["2","4","2","4","2","2","4","1","1"],
    ["2","4","2","1","3","3","4","3","2"],
    ["1","4","2","1","2","1","4","3","5"],
]
  
# Iterate through each data
for data in datas:
    # Open URL
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeqPpV4uVey9u81aBa1Eh6kjtD8vsAQlmtS3kBVi7WRTSGiMA/viewform')
  
    # wait for one second, until page gets fully loaded
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div["+data[0]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div["+data[1]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div["+data[2]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div["+data[3]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div["+data[4]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div["+data[5]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div["+data[6]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label["+data[7]+"]").click();
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label["+data[8]+"]").click();
    
    # /html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]
    # click on submit button
    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
  
    # driver.refresh()
    # time.sleep(5)
  
# close the window
driver.close()

# /html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]
# freebirdFormviewerComponentsQuestionBaseRoot
# freebirdFormviewerComponentsQuestionBaseRoot
# /html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]
# # Initialize count is zero
#     count = 0
  
#     # contain input boxes
#     textboxes = driver.find_elements_by_class_name(
#         "quantumWizTextinputPaperinputInput")
  
#     # contain textareas
#     textareaboxes = driver.find_elements_by_class_name(
#         "quantumWizTextinputPapertextareaInput")
  
#     # Iterate through all input boxes
#     for value in textboxes:
#         # enter value
#         value.send_keys(data[count])
#         # increment count value
#         count += 1
  
#     # Iterate through all textareas
#     for value in textareaboxes:
#         # enter vlaue
#         value.send_keys(data[count])
#         # increment count value
#         count += 1
