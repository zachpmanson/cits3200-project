from email.mime import image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#for waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Chrome options
from selenium.webdriver.chrome.options import Options
import time
import os
import cv2

#Retrieve map image and url
def getMaps(place, count) :

    # headless mode
    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    # relative path - chromedriver must be in same file as this component
    # chromedriver is dependent on specific version of chrome: https://chromedriver.chromium.org/downloads

    # https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/
    # xattr -d com.apple.quarantine /Users/danteshabani/Desktop/cits3200-project/chatbot/chromedriver (for mac security issue)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    PATH = os.path.join(script_dir, "chromedriver")
    driver = webdriver.Chrome(PATH, options=op)

    driver.get("https://www.google.com/maps/")

    search = driver.find_element(By.ID, "searchboxinput")

    search.send_keys(place)
    search.send_keys(Keys.RETURN)

    time.sleep(4)
    mapf = "msc/map_sc" + str(count) + ".png"
    driver.get_screenshot_as_file(mapf)

    url = driver.current_url 
    return url

#Resize image
def resizeMap(imagefn, count) :
    img=cv2.imread(imagefn)

    scale=0.225
    w=int(img.shape[1]*scale)
    h=int(img.shape[0]*scale)
    dim=(w,h)

    resized=cv2.resize(img, dim,interpolation=cv2.INTER_AREA)

    cv2.imwrite('msc/map_sc'+str(count)+'.png', resized)

    return 0