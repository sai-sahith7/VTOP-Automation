from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait,Select
ext = webdriver.ChromeOptions()
ext.add_extension("extension_4_9_1_0.crx")
driver = webdriver.Chrome(options=ext)
wait = WebDriverWait(driver,100)
website = "https://vtop.vit.ac.in/vtop/initialProcess"
driver.get(website)
wait.until(ec.visibility_of_element_located((By.LINK_TEXT,"Login to VTOP"))).click() # first log-in button
wait.until(ec.visibility_of_element_located((By.XPATH,'//button[@onclick="openPage()"]'))).click() #second log-in button
username = wait.until(ec.visibility_of_element_located((By.ID,"uname"))) #entering username
password = wait.until(ec.visibility_of_element_located((By.ID,"passwd"))) #entering password
signinbn = wait.until(ec.visibility_of_element_located((By.ID,"captcha"))) #for clicking sign-in button
username.send_keys("*Enter your student-ID*")  #***** USER INSTRUCTION - Edit your student-ID in this line *****
password.send_keys("*Enter your VTOP password*") #***** USER INSTRUCTION - Edit your VTOP password in this line *****
signinbn.click()
def until_courseoption():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="menu-toggle"]'))).click() #clicking on menu button
    wait.until(ec.visibility_of_element_located((By.XPATH,'//a[@href="#MenuBody6"]'))).click() #clicking on academics
    wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="ACD0045"]'))).click() #clicking on course page
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter Your Semester Code Here*"]'))).click() #***** USER INSTRUCTION - Edit your Semester code in this line (Example : VL20212201) *****
def course1():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #***** USER INSTRUCTION - Edit your Course-id in this line (Example:- VL2021220105887) *****
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #***** USER INSTRUCTION - Edit your Class-id in this line (Example:- VL2021220105879) *****

# ***** USER INSTRUCTION - Follow the same steps for all the courses below *****

def course2():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #selecting Course-2
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def course3():
    wait.until(ec.visibility_of_element_located((By.XPATH, '//option[@value="*Enter your Course-ID here*"]'))).click()  # selecting Course-3
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def course4():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #selecting Course-4
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof.
def course5():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #selecting Course-5
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def course6():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #selecting Course-6
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def course7():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #selecting Course-7
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def course8():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() # selecting Course-8
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def course9():
    wait.until(ec.visibility_of_element_located((By.XPATH,'//option[@value="*Enter your Course-ID here*"]'))).click() #selecting Course-9
    wait.until(ec.visibility_of_element_located((By.XPATH,'//tr[td="*Enter your Class-ID here*"]//button'))).click() #selecting prof
def all():
    until_courseoption()
    course1()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(website)
    until_courseoption()
    course2()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get(website)
    until_courseoption()
    course3()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[3])
    driver.get(website)
    until_courseoption()
    course4()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[4])
    driver.get(website)
    until_courseoption()
    course5()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[5])
    driver.get(website)
    until_courseoption()
    course6()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[6])
    driver.get(website)
    until_courseoption()
    course7()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[7])
    driver.get(website)
    until_courseoption()
    course8()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[8])
    driver.get(website)
    until_courseoption()
    course9()
all()