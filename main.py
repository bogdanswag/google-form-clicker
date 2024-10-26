import random, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-crash-reporter")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-in-process-stack-traces")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--output=/dev/null")
chrome_options.add_argument("--disable-application-cache")


driver = webdriver.Chrome(options=chrome_options)

url = 'https://google-form-url'
driver.get(url)

for clicks in range(500): # choose your range
    groups = [
        [
            driver.find_element(By.XPATH, '//*[@id="i5"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i8"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i11"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i18"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i21"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i24"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i31"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i34"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i37"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i44"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i47"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i50"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i57"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i60"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i63"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i70"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i73"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i76"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i83"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i86"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i89"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i96"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i99"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i102"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i109"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i112"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i115"]/div[3]/div')
        ],
        [
            driver.find_element(By.XPATH, '//*[@id="i122"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i125"]/div[3]/div'),
            driver.find_element(By.XPATH, '//*[@id="i128"]/div[3]/div')
        ]
    ]

    for group in groups:
        random_button = random.choice(group)
        ActionChains(driver).move_to_element(random_button).click(random_button).perform()

    send_button = driver.find_element(By.XPATH, '//div[@role="button" and contains(@class, "uArJ5e") and .//span[text()="Отправить"]]')
    ActionChains(driver).move_to_element(send_button).click(send_button).perform()

    time.sleep(2)

    driver.get(url)


driver.quit()
