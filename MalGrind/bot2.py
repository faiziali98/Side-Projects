import time
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
import random
# opts = Options()
# opts.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0")
# opts.add_argument('--proxy-server=http://127.0.0.1:9050')

profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
# display = Display (visible=0, size=(800,600))
# display.start()

driver = webdriver.Firefox(profile)
url = "https://www.youtube.com/watch?v=jdvNRrEUfg8"

def view_page():
	# export PATH=$PATH:/home/saimsalman/Desktop/ToDo    
    driver.get(url)
    # random.randint(5,10)
    time.sleep(10)
    print ("Page viewed")
    # driver.quit()

for i in range(100):
    view_page()