from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import traceback
import os

os.system('cls')

while True:
    try:
        # Load the data
        data = pd.read_csv('BN.csv')
        datasaved = pd.read_csv('output2.csv')
        nowitem = 1
        datasave = {'id': [], 'name': []}

        for i in data['Item_id']:
            # Path to ChromeDriver and Brave browser
            chrome_driver_path = "C:/Users/taois/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with actual ChromeDriver path
            brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with actual Brave path

            # Set up ChromeOptions to use Brave in headless mode
            options = Options()
            options.binary_location = brave_path  # Point to Brave's executable
            options.add_argument("--headless")  # Run the browser in headless mode

            # Initialize WebDriver with Brave
            service = Service(chrome_driver_path)
            driver = webdriver.Chrome(service=service, options=options)

            # Open the website
            driver.get("https://www.ulta.com/shop/makeup/face/foundation")

            # Wait for and close any pop-ups (if present)
            try:
                accept_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
                )
                accept_button.click()
            except:
                print("No pop-up to close.")

            try:
                accept_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Product search']"))
                )
                accept_button.click()
            except:
                print("No pop-up to close.")

            # Find the search input field
            search_input = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search products and more']"))
            )

            # Enter the search query
            re = f'{len(datasaved)+nowitem}:{len(data) - len(datasaved)} || {round((len(datasaved)+nowitem) / (len(data)), 2) * 100}%'
            nowitem += 1
            search_query = i
            search_input.send_keys(search_query)

            # Simulate pressing the Enter key to submit the search
            search_input.send_keys(Keys.RETURN)

            # Initialize product_name_element variable
            product_name_element = None

            # Try to find the product name using the first XPath
            try:
                product_name_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[@class='ProductInformation']//a[contains(@class, 'pal-c-Link') and contains(@class, 'pal-c-Link--primary') and contains(@class, 'pal-c-Link--compact')]")
                    )
                )
                print(product_name_element)
            except TimeoutException:
                # If the product name element is not found, check if "No results found" message is present
                try:
                    no_results_message = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//div[@class='NullSearchResult']//p[contains(text(), 'No results found')]")
                        )
                    )
                    if no_results_message:
                        print(f"No results found for {search_query}")
                        data = data[data['Item_id'] != i]
                        data.reset_index(drop=True).to_csv('BN.csv', index=False)
                        continue  # Skip to the next search query
                    else:
                        no_results_message = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, f"//a[@class='pal-c-Link']//span[contains(text(), '{i}')]"))
                                )
                        no_results_message.click()
                    

                except TimeoutException:
                    print("Neither product name nor 'No results found' message could be found.")

            # Only print and save the product name if it was successfully found
            if product_name_element:
                print(re, "Product Name:", product_name_element.text)

                # Save the product details
                datasave.setdefault('id', []).append(i)
                datasave.setdefault('name', []).append(product_name_element.text)

                # Convert to DataFrame and save to CSV
                df = pd.DataFrame(datasave)
                df = pd.concat([datasaved, df], axis=0)
                df.to_csv('output3.csv', index=False)
            else:
                print(f"Could not find product name for {search_query}")

            # Close the browser
            driver.quit()

        print("Batch completed successfully.")
        # Add a delay to avoid spamming the server with requests
        time.sleep(5)  # Adjust the sleep time as needed

    except Exception as e:
        # Print the error traceback for debugging
        print(f"Error occurred: {str(e)}")
        print("Stack trace:", traceback.format_exc())
        
        # Wait for a short time before restarting the loop to avoid rapid failure retries
        print("Restarting the process...")
