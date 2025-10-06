from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def open_url(url: str):
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--start-maximized')

    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--disable-extensions")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)
    return driver

def captcha_finder(driver):
    for i in range(5):
        try:
            captcha_img = WebDriverWait(driver, 5).until(
                            EC.visibility_of_element_located(
                                (By.ID, "c_login_formcaptcha_CaptchaImage")
                            )
                        )
            captcha_img.screenshot(f"images/{i:02d}.png")

            reload_img = driver.find_element(By.ID, "c_login_formcaptcha_ReloadIcon")
            reload_img.click()

        except Exception as e:
            print(f"Error with Selenium: {e}")
            return None

    driver.quit()

if __name__ == "__main__":
    captcha_url = "https://nut.uk.ac.ir/"
    driver = open_url(captcha_url)
    captcha_finder(driver)