from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setup Selenium WebDriver
chrome_driver_path = "C:/Users/unkno/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with your ChromeDriver path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with your Brave browser path

# Configure options for the WebDriver
options = Options()
options.binary_location = brave_path
# Uncomment the line below if you want to run in headless mode
# options.add_argument("--headless")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Read product links from a CSV file (update the file name as needed)
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# Check for rows where `faceoff_positive` is null
urls = df['product_link'][df['faceoff_positive'].isnull()]

# Prepare the dictionary to store scraped data
dana = {"Item_id": [], "faceoff_positive": []}

try:
    for url in urls:
        driver.get(url)
        
        try:
            # Wait for the `faceoff_positive` section to appear
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section.pr-faceoff-positive"))  # Update the selector if necessary
            )
            faceoff_text = element.text.strip()
        except:
            faceoff_text = "N/A"  # If the element is not found

        # Extract the Item ID from the URL (assuming it's the last 7 characters before "#reviews")
        if "sku=" in url:
            item_id = url.split("sku=")[-1].split("#")[0]
        else:
            item_id = "Unknown"

        # Append to the data dictionary
        dana["Item_id"].append(item_id)
        dana["faceoff_positive"].append(faceoff_text)
        print(f"Scraped Item ID: {item_id}, Faceoff Positive: {faceoff_text}")

finally:
    driver.quit()

# Convert the dictionary to a DataFrame and save to CSV
df_result = pd.DataFrame(dana)
df_result.to_csv("scraped_faceoff_positive.csv", index=False)
print("Scraping completed. Data saved to 'scraped_faceoff_positive.csv'")
