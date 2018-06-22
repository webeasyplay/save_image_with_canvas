import os
import base64, re
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()


def base64_to_image(base64_str, image_path=None):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    if image_path:
        img.save(image_path)


def save_captcha():
    driver.switch_to.frame(1)
    try:
        img_data = driver.execute_script('return localStorage.getItem("imgInfo")')
        base64_to_image(img_data,"CAPTCHA.png")
    except Exception as e:
        print(str(e))

driver_path = os.path.join(os.getcwd(), 'chromedriver')
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
driver.get("https://waste.epa.gov.tw/prog/IndexFrame.asp?Func=2")
save_captcha()
