#Mi Trade Bot to Buy and close a positon Made by pushpender_3740
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time,os


def main():
    os.system('run.bat')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress","localhost:9000")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get("https://app.mitrade.com/")
    print('''Choose the login option :
            1. through google account
            2. E-mail and password''')
    ln=input()
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break
    page=driver.page_source
    while True:
        if("Create Account" in page or "Log In" in page):
            if ln=='1':
                login_go(driver)
                break
            elif ln=='2':
                login(driver)
                break
            else:
                print("!!wrong Input!!")
        else:
            break
    while True:
        print('''Hi! Welcome to the Trading Bot
                choose the Name for buying
                1. CHF/JPY
                2. GBP/USD
                3. SPX500''')
        ch=input("Enter Choice: ")
        tim=input("Enter the time(in seconds) after which you wants to close the position: ")
        if(ch=='1'):
            while True:
                try:
                    quantity=float(input("Enter the quantity between 0.01 to 30.00 of CHF/JPY to buy : "))
                    print(quantity)
                    if quantity>=0.01 and quantity<=30.00:
                        nam="CHF/JPY"
                        lev="30x"
                        page=driver.page_source
                        if 'Mitrade website uses necessary cookies to provide you with more personalised service. For more details, please refer to "Cookies" in our' in page:
                            driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/button').click()
                        buy(driver,nam,str(quantity),lev)
                        break
                    else:
                        hgchgcv
                except KeyboardInterrupt:
                    exit()
                except Exception as e:
                    print(e)
                    print("!!wrong input1!!")
            break
        elif(ch=='2'):
            while True:
                try:
                    quantity=float(input("Enter the quantity between 0.01 to 30.00 of GBP/USD to buy : "))
                    if quantity>=0.01 and quantity<=30.00:
                        nam="GBP/USD"
                        lev="30x"
                        page=driver.page_source
                        if 'Mitrade website uses necessary cookies to provide you with more personalised service. For more details, please refer to "Cookies" in our' in page:
                            driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/button').click()
                        
                        buy(driver,nam,str(quantity),lev)
                        break
                    else:
                        hgchgcv
                except KeyboardInterrupt:
                    exit()
                except Exception as e:
                    print(e)
                    print("!!wrong input!!")
            break
        elif(ch=='3'):
            while True:
                try:
                    quantity=int(input("Enter the quantity between 1 to 100 of SPX500 to buy : "))
                    if (quantity>=1 and quantity<=100):
                        nam="SPX500"
                        lev="20x"
                        page=driver.page_source
                        if 'Mitrade website uses necessary cookies to provide you with more personalised service. For more details, please refer to "Cookies" in our' in page:
                            driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/button').click()
                        
                        buy(driver,nam,str(quantity),lev)
                        break
                    else:
                        hgchgcv
                except KeyboardInterrupt:
                    exit()
                except Exception as e:
                    print(e)
                    print("!!wrong input!!")
            break
        else:
            print("!!Wrong input!!")
    
    while True:
        time.sleep(int(tim))
        try:
            clos(driver)
        except:
            print("No position is open Right Now")
        buy(driver,nam,str(quantity),lev)
        print("New Position Opened")
    # driver.close()
def login_go(driver):
    em=open("./gmail.txt",'r')
    email=em.read()
    em.close()
    pas=open("./gpassword.txt",'r')
    password=pas.read()
    pas.close()
    driver.get("https://app.mitrade.com/sign-in")
    main_window_handle = None
    while not main_window_handle:
        main_window_handle = driver.current_window_handle
    driver.find_element_by_id("gaSignIn").click()
    signin_window_handle = None
    while not signin_window_handle:
        for handle in driver.window_handles:

            if handle != main_window_handle:
                signin_window_handle = handle
                break
    driver.switch_to.window(signin_window_handle)
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        pass
    driver.switch_to.window(main_window_handle)
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break
    print("Now you have 60 seconds to select your account type(Live/Demo) on the browser Window")
    time.sleep(60)
    driver.get("https://app.mitrade.com/")
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break

def login(driver):
    em=open("./email.txt",'r')
    email=em.read()
    em.close()
    pas=open("./password.txt",'r')
    password=pas.read()
    pas.close()
    driver.get("https://app.mitrade.com/sign-in")
    for i in range(0,100):
        driver.find_element_by_id("email").send_keys(Keys.BACKSPACE)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("password").send_keys(Keys.ENTER)
    time.sleep(3)
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break
    print("Now you have 60 seconds to select your account type(Live/Demo) on the browser Window")
    time.sleep(60)
    driver.get("https://app.mitrade.com/")
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break

def buy(driver,name,quantity,lev):
    try:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div/a[1]').click()
    except:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/a[1]').click()
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break
    for i in range(0,50):
        driver.find_element_by_name("search").send_keys(Keys.BACKSPACE)
    driver.find_element_by_name("search").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="main-body"]/div/div[1]/div[1]/div[1]/div[3]/div').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="hoverBtn"]/button[2]').click()
    for i in range(0,6):
        driver.find_element_by_xpath('//*[@id="main-body"]/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/input').send_keys(Keys.BACKSPACE)
    driver.find_element_by_xpath('//*[@id="main-body"]/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/input').send_keys(quantity)
    driver.find_element_by_xpath('//*[@id="main-body"]/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/div/div[1]/div/div/div/div[3]/div/div/div/div/div/span[2]').click()
    time.sleep(1)
    vals=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[1]/div/div')
    all_vals=vals.find_elements_by_tag_name("div")
    for i in all_vals:
        txt=i.text
        if txt==lev:
            i.click()
            break
    buy_b=driver.find_element_by_xpath('//*[@id="main-body"]/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[3]/div/div[2]/button')
    buy_b.location_once_scrolled_into_view
    buy_b.click()

def clos(driver):
    page=driver.page_source
    if("Create Account" in page or "Log In" in page):
        login(driver)
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div/a[2]').click()
        except:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[1]/div/a[2]').click()
    
    else:    
        driver.get("https://app.mitrade.com/positions")
    while True:
        try:
            driver.find_element_by_id("app-load")
        except:
            break
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="rc-tabs-0-panel-openPositions"]/ul/li').click()
    driver.find_element_by_xpath('//*[@id="main-body"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="main-body"]/div/div/div[2]/div/div/div/div[1]/div[3]/div/div[3]/div/div[2]/button').click()
if __name__ == "__main__":
    main()

