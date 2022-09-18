
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def launchBrowser():

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    
    driver.get('https://research-repository.uwa.edu.au/en/persons/yulia-shiikha')
    
    return driver
        
if __name__ == "__main__":    
    driver = launchBrowser()