from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Set up WebDriver (replace 'chromedriver' with your driver path if necessary)
chrome_driver_path = "C:/Users/unkno/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with your ChromeDriver path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with your Brave browser path

# Configure options for the WebDriver
options = Options()
options.binary_location = brave_path  # Point to Brave's executable
# options.add_argument("--headless")  # Run in headless mode
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL of the page to scrape
url = 'https://www.ulta.com/p/shape-tape-full-coverage-concealer-xlsImpprod14251035?sku=2501208#reviews',''  # Replace with the actual URL
driver.get(url)

dana = {"Item_id":[], "faceoff-positive":[]}

try:
    # Wait for the <h6> element to be present within the specified <div>
    timeout = 10  # Set your desired timeout in seconds
    question_text = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "section.pr-faceoff-positive")) 
    )
    print("Question Text:", question_text.text) 
    dana["faceoff-positive"].append(question_text.text)
    dana['Item_id'].append(url[-7:])
except Exception as e:
    print("Error:", e)
finally:
    driver.quit()

df_result = pd.DataFrame(dana)
df_result.to_csv('scraped_faceoff_positive.csv')