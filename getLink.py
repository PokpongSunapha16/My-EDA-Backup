# import re
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# datalink = {'link':[]}
# for i in range(50):
#     # URL of the webpage
#     url = BASE_URL = f"https://www.ulta.com/shop/makeup/face?page={i}"

#     # Fetch the webpage content
#     response = requests.get(url)
#     response.raise_for_status()

#     # Parse the HTML
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find all links
#     links = soup.find_all('a', href=True)

#     # Extract links with 'sku=<ID>'
#     sku_links = []
#     for link in links:
#         match = re.search(r'sku=(\d+)', link['href'])
#         if match:
#             sku_links.append(link['href'])

#     # Print results
#     # print("Dynamic links with SKU:")
#     for sku_link in sku_links:
#         # print(sku_link)
#         datalink['link'].append(sku_link)
# # data = pd.Series(sku_links,name='Link')
# data = pd.DataFrame(datalink)
# data.to_csv('ThisLink.csv')


# import time
# import pandas as pd
# from selenium import webdriver
# import re
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (adjust the path to the driver)
# chrome_driver_path = "C:/Users/taois/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with actual ChromeDriver path
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with actual Brave path
# # Set up ChromeOptions to use Brave in headless mode
# options = Options()
# options.binary_location = brave_path  # Point to Brave's executable
# options.add_argument("--headless")  # Run the browser in headless mode
# options.add_argument("--disable-gpu")  # Disable GPU acceleration (often required for headless mode)
# # Initialize WebDriver with Brave
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=options)
# # Open the target webpage
# driver.get("https://www.ulta.com")

# # Get page source
# page_source = driver.page_source

# # Extract links with regex
# sku_links = re.findall(r'href="([^"]*sku=\d+)"', page_source)

# # Print results
# print("Dynamic links with SKU:")
# for link in sku_links:
#     print(link)

# # Close the browser
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
# import re
# from urllib.parse import urljoin

# # Base URL for Ulta
# for i in range(30):
#     BASE_URL = f"https://www.ulta.com/shop/makeup/face?page={i}"
#     # Initialize the Selenium WebDriver
#     chrome_driver_path = "C:/Users/taois/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with actual ChromeDriver path
#     brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with actual Brave path
#     # Set up ChromeOptions to use Brave in headless mode
#     options = Options()
#     options.binary_location = brave_path  # Point to Brave's executable
#     options.add_argument("--headless")  # Run the browser in headless mode
#     # options.add_argument("--disable-gpu")  # Disable GPU acceleration (often required for headless mode)
#     # Initialize WebDriver with Brave
#     service = Service(chrome_driver_path)
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.get(BASE_URL)

#     # Wait for the page to load completely
#     time.sleep(5)  # Adjust as needed depending on your internet speed

#     # Function to extract links with 'sku=<ID>' from the current page
#     def extract_sku_links(page_source):
#         # Regex to find links with 'sku=<ID>'
#         raw_links = re.findall(r'href="([^"]*sku=\d+)"', page_source)
#         # Convert relative links to absolute
#         full_links = [urljoin(BASE_URL, link) for link in raw_links]
#         return full_links

#     # List to store all product links
#     all_sku_links = []

#     # Pagination handling
#     while True:
#         # Get the page source
#         page_source = driver.page_source

#         # Extract links from the current page
#         sku_links = extract_sku_links(page_source)
#         all_sku_links.extend(sku_links)

#         # Try to find and click the "Next" button
#         try:
#             next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next']")  # Update selector if necessary
#             next_button.click()
#             time.sleep(3)  # Wait for the next page to load
#         except:
#             # Break the loop if the "Next" button is not found
#             break

#     # Remove duplicate links
#     all_sku_links = list(set(all_sku_links))

#     # Print all extracted links
#     print("Extracted SKU Links:")
#     for link in all_sku_links:
#         print(link)

#     # Close the browser
#     driver.quit()

# import requests
# import pandas as pd

# def check_links(link_list):
#     results = []

#     for link in link_list:
#         try:
#             # Check the link status
#             response = requests.head(link, allow_redirects=True, timeout=5)
#             status_code = response.status_code
#             results.append((link, status_code))
#             print(f"Link: {link} - Status Code: {status_code}")
#         except requests.exceptions.RequestException as e:
#             results.append((link, str(e)))
#             print(f"Error checking link {link}: {e}")

#     return results

# # Example list of links
# links_to_check = pd.read_csv('data.csv')
# links_to_check = links_to_check['product_link']
# # Run the check
# results = check_links(links_to_check)

# # Print summary
# print("\nSummary:")
# for link, status in results:
#     print(f"{link} - {status}")




# from bs4 import BeautifulSoup
# import requests

# # Make a request to the webpage
# url = 'https://www.ulta.com/p/charlottes-beautiful-skin-foundation-pimprod2043365?sku=2619495'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all elements with the specified classes
# elements = soup.find_all('span', class_='Text-ds Text-ds--body-1 Text-ds--left Text-ds--black')
# elements2 = soup.find_all('span', class_='Text-ds Text-ds--title-5 Text-ds--left Text-ds--black')

# # Combine both lists and iterate
# for element, element2 in zip(elements, elements2):
#     print(element.get_text(strip=True), element2.get_text(strip=True))
#######################################################################################
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # List of SKUs
# # skus = ['2619495', '2622206']
# urls = pd.read_csv('data.csv')
# urls = urls['product_link']
# # Base URL
# base_url = 'https://www.ulta.com/p/'
# data = {'Product_name':[],'Brand':[],'Item_id':[]}
# # Iterate over each SKU and scrape the corresponding page
# for url in urls:
#     response = requests.get(url)
    
#     # Check if the page was successfully retrieved
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title = soup.find('span', {'class': 'Text-ds Text-ds--title-5 Text-ds--left Text-ds--black'})
#         span_tag = soup.find_all('span', {'class':'Text-ds Text-ds--body-1 Text-ds--left Text-ds--black'})      
#         item_id = soup.find_all('p', {'class':'Text-ds Text-ds--body-3 Text-ds--left Text-ds--neutral-600'})      
# ############################
#         if len(span_tag) >= 3:
#             second_span_tag = span_tag[3]
#             a_tag = second_span_tag.find('a', {'class': 'pal-c-Link pal-c-Link--primary pal-c-Link--compact'})
#             print(f'Brand || {a_tag.get_text(strip=True)}')
#             data['Brand'].append(a_tag.get_text(strip=True))
#         else:
#             print("No Brand NAN")
#             data['Brand'].append('nan') 

# ############################

#         # second_span_tag = span_tag[3]
#         # a_tag = second_span_tag.find('span', {'class': 'Text-ds Text-ds--body-3 Text-ds--left Text-ds--black'})
#         print(f'Item_id || {url[-7:]}')
#         data['Item_id'].append(url[-7:]) 
# ############################
#         if title:
#             # print(f'Product for SKU {sku}: {title.get_text(strip=True)}')
#             print(f'Title || {title.get_text(strip=True)}')
#             data['Product_name'].append(title.get_text(strip=True))
            
#         else:
#             # pass
#             # print(f'Product title for SKU {url} not found.')
#             print(f'No Title NAN')
#             data['Product_name'].append('nan')
            
#     else:
#         print(f'Failed to retrieve page for SKU {url}. Status Code: {response.status_code}')
#         # print(f'Item_id || {url[-7:]}')
#         data['Item_id'].append(url[-7:])
#         data['Product_name'].append('nan')
#         data['Brand'].append('nan')

# data = pd.DataFrame(data)
# data.to_csv('save_data.csv')











#----------------------------------------------------------------------------------------------------------------





import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# List of URLs (replace with actual URLs or use a CSV)
# urls = pd.read_csv('data.csv')
# urls = urls['product_link']
urls = pd.read_csv('ThisLink.csv')
urls = urls['link']
numof = len(urls)
nownum = 1
data = {'Product_name':[], 'Brand':[], 'Item_id':[], 'Swiper_count':[], 'Price':[]}

# Iterate over each URL and scrape the corresponding page
for url in urls:
    response = requests.get(url, timeout=15)
    
    # Check if the page was successfully retrieved
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Scraping product details
        title = soup.find('span', {'class': 'Text-ds Text-ds--title-5 Text-ds--left Text-ds--black'})
        span_tag = soup.find_all('span', {'class':'Text-ds Text-ds--body-1 Text-ds--left Text-ds--black'})
        item_id = soup.find_all('p', {'class':'Text-ds Text-ds--body-3 Text-ds--left Text-ds--neutral-600'})
        
        ############################
        # Scraping the Brand (if available)
        if len(span_tag) >= 3:
            second_span_tag = span_tag[3]
            a_tag = second_span_tag.find('a', {'class': 'pal-c-Link pal-c-Link--primary pal-c-Link--compact'})
            # print(f'|Brand = {a_tag.get_text(strip=True)}|')
            data['Brand'].append(a_tag.get_text(strip=True))
        else:
            print("No Brand NAN")
            data['Brand'].append('nan')
        ############################

        # Scraping the Item ID (from the URL)
        # print(f'|Item_id = {url[-7:]}|')
        data['Item_id'].append(url[-7:])
        
        ############################
        # Scraping the Title
        if title:
            # print(f'|Title = {title.get_text(strip=True)}|')
            data['Product_name'].append(title.get_text(strip=True))
        else:
            print(f'No Title NAN')
            data['Product_name'].append('nan')
            
        ############################
        # Scraping swiper-slide count
        swiper_wrapper = soup.find('div', class_='swiper-wrapper')
        if swiper_wrapper:
            swiper_items = swiper_wrapper.find_all('div', class_='swiper-slide')
            swiper_count = len(swiper_items)
            # print(f'|Swiper Count = {swiper_count}|')
            data['Swiper_count'].append(swiper_count)
        else:
            print('No swiper-wrapper found')
            data['Swiper_count'].append('nan')
        
        ############################
        # Scraping the Price
        product_pricing = soup.find_all('div', {'class': 'ProductPricing'})
        product_pricing = product_pricing[0] if product_pricing else None

        if product_pricing:
            # Try finding the price with the first class
            price = product_pricing.find('span', {'class': 'Text-ds Text-ds--title-5 Text-ds--left Text-ds--black'})
            
            # If not found, try the second class
            if not price:
                price = product_pricing.find('span', {'class': 'Text-ds Text-ds--title-5 Text-ds--left Text-ds--magenta-500'})
            
            if price:
                # print(f'|Price = {price.get_text(strip=True)}|')
                data['Price'].append(price.get_text(strip=True))
            else:
                print('No Price inside ProductPricing NAN')
                data['Price'].append('nan')
        else:
            print('No ProductPricing div found')
            data['Price'].append('nan')

    else:
        print(f'Failed to retrieve page for {url}. Status Code: {response.status_code}')
        data['Item_id'].append(url[-7:])
        data['Product_name'].append('nan')
        data['Brand'].append('nan')
        data['Swiper_count'].append('nan')
        data['Price'].append('nan')
    # data = pd.DataFrame(data)
    os.system('cls')
    print('-' * (len(data['Product_name'][-1])+20)
        ,'\n',
        '|Item_id =',data['Item_id'][-1],'\n',
        '|Brand =',data['Brand'][-1],'\n',
        '|Swiper =',data['Swiper_count'][-1],'\n',
        '|Title =',data['Product_name'][-1],'\n',
        '|Price =',data['Price'][-1],
        # f'|Item_id = {data[['Item_id']]}|','\n',
        # f'|Brand = {data.Brand[-1]}|','\n',
        # f'|Swiper Count = {data.Product_name[-1]}|','\n',
        # f'|Title = {data.Swiper_count[-1]}|','\n',
        # f'|Price = {data.Price[-1]}|'
        )
    print('-' * (len(data['Product_name'][-1])+20))
    print('=' * int((int(nownum / numof)*70)+1),f'Scrap process now :{round(round(nownum / numof,3)*100,2)} %')
    nownum += 1
# Save the collected data to a CSV file
data = pd.DataFrame(data)
data.to_csv('save_dataNews.csv', index=False)

