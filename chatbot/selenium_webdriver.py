
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def launchBrowser():

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    #driver.get('https://www.google.com.au')
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    
    
    print('Open Successful...!!')
    print(driver.title)
    print(driver.current_url)
    #driver.quit()
    return driver
        
    
driver = launchBrowser()