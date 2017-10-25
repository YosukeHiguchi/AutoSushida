import time
import sys
import pyocr
import pyocr.builders
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))


print("Starting chrome...")

serv = service.Service('./chromedriver')
serv.start()
capabilities = {'chrome.binary': '/Applications/Google\ Chrome.app'};

driver = webdriver.Remote(serv.service_url, capabilities)
driver.get('http://neutral.x0.com/home/sushida/play2.html')

driver.execute_script("document.body.style.zoom = '1.5'")

# set up game by hand
time.sleep(15)

# Start game
driver.find_element_by_tag_name("embed").send_keys(Keys.SPACE)

# ready set go
time.sleep(2)

while True:
    driver.save_screenshot("txt.png")
    im = Image.open("txt.png")
    box = (202, 450, 922, 490)
    im = im.crop(box)

    txt = tool.image_to_string(
        im,
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )

    print(txt)
    for t in txt.split():
        if (len(t) > 1):
            print(t)
            driver.find_element_by_tag_name("embed").send_keys(txt)
            break

    time.sleep(0.5)

driver.quit()