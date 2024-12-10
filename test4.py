from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup Selenium WebDriver
chrome_driver_path = "C:/Users/unkno/scoop/apps/chromedriver/current/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

options = Options()
options.binary_location = brave_path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Read product links from CSV
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# Check for rows where `faceoff_positive` is null
urls = df['product_link'][df['faceoff_positive'].isnull()]  # ใช้ 'faceoff_positive' แทน 'faceoff-positive'
print(f"Found {len(urls)} URLs to scrape.")  # พิมพ์จำนวน URL ที่จะ scrap

# Prepare the dictionary to store scraped data
dana = {"Item_id": [], "faceoff_positive": []}  # ใช้ 'faceoff_positive' แทน 'faceoff-positive'

try:
    for url in urls:
        driver.get(url)
        
        # Wait for the `faceoff_positive` section to appear
        try:
            # Increase the wait time for dynamic content
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section.pr-faceoff-positive"))
            )
            
            # Get the element text
            element = driver.find_element(By.CSS_SELECTOR, "section.pr-faceoff-positive")
            faceoff_text = element.text.strip()
        except Exception as e:
            faceoff_text = "N/A"
            print(f"Error finding element for {url}: {e}")
            
        # Extract Item ID
        item_id = url.split("sku=")[-1].split("#")[0] if "sku=" in url else "Unknown"
        
        # Append to dictionary
        dana["Item_id"].append(item_id)
        dana["faceoff_positive"].append(faceoff_text)
        print(f"Scraped Item ID: {item_id}, Faceoff Positive: {faceoff_text}")
        
        # Optionally print the page source for debugging
        print(driver.page_source)

finally:
    # Print dana to check data before saving
    print(dana)
    
    # Save data to CSV before quitting the driver
    df_result = pd.DataFrame(dana)
    df_result.to_csv("MYscraped_faceoff_positive.csv", index=False)  # ชื่อไฟล์ผลลัพธ์
    print("Scraping completed. Data saved to 'MYscraped_faceoff_positive.csv'")
    
    driver.quit()
