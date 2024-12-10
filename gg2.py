from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np  # Import numpy to use np.nan

# Setup Selenium WebDriver (Chrome in this case)
options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode (without opening the browser window)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
columns_to_check = ['rating','num_reviews','description','pros','cons','best_uses','describe_yourself']
urls = df['product_link'][df[columns_to_check].isnull().any(axis=1)]

data = []

for url in urls:
    print(f"Processing URL: {url}")

    try:
        driver.get(url + '#reviews')
        # web1 = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, 'reviewsSnap'))
        # )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'pr-review-snapshot') and contains(@class, 'pr-snapshot-mobile')]")
                                           )
        )
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        reviews_snapshot = soup.find('div', {'class': 'pr-review-snapshot-header pr-review-snapshot-content-block'})

        try:
            rating = reviews_snapshot.find('div', class_='pr-snippet-stars').find('div', class_='pr-snippet-rating-decimal').text.strip()
            review_count = reviews_snapshot.find('span', class_='pr-snippet-review-count').text.strip()
            recommendation_percentage = reviews_snapshot.find('span', class_='pr-reco-value').text.strip()
            if rating:
                print('found rating')
            else:
                print('not found rating')
            if review_count:
                print('found review_count')
            else:
                print('not found review_count')
            if recommendation_percentage:
                print('found recommendation_percentage')
            else:
                print('not found recommendation_percentage')
            ratings_distribution = []
            histogram_items = reviews_snapshot.find_all('li', class_='pr-ratings-histogram-list-item')
            for item in histogram_items:
                star_rating = item.find('p', class_='pr-histogram-label').text.strip()
                review_count = item.find('p', class_='pr-histogram-count').text.strip()
                ratings_distribution.append(f"{star_rating}: {review_count} reviews")
            pros = [item.text.strip() for item in reviews_snapshot.find_all('dd', class_=' ')]
            data.append({
                'Item_id': url[-7:],
                'url': url,
                'rating': rating,
                'review_count': review_count,
                'recommendation_percentage': recommendation_percentage,
                'ratings_distribution': "; ".join(ratings_distribution),
                'pros': "; ".join(pros)
            })
            print(f"Item_id: {url[-7:]}")
            print(f"Rating: {rating}")
            print(f"Total Reviews: {review_count}")
            print(f"Recommendation: {recommendation_percentage}")
            print("Ratings Distribution:")
            for dist in ratings_distribution:
                print(dist)
            print("\nPros:")
            for pro in pros:
                print(pro)

        except AttributeError:
            data.append({
                'Item_id': url[-7:],
                'url': url,
                'rating': np.nan,
                'review_count': np.nan,
                'recommendation_percentage': np.nan,
                'ratings_distribution': np.nan,
                'pros': np.nan
            })
            print(f"Could not extract information for {url}")

    except Exception as e:
        print(f"Error loading URL {url}: {e}")
        data.append({
            'Item_id': url[-7:],
            'url': url,
            'rating': np.nan,
            'review_count': np.nan,
            'recommendation_percentage': np.nan,
            'ratings_distribution': np.nan,
            'pros': np.nan
        })

# Convert the collected data into a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('product_reviews.csv', index=False)

# Close the driver
driver.quit()



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from concurrent.futures import ThreadPoolExecutor, TimeoutError
# import pandas as pd
# import numpy as np

# # Setup Selenium WebDriver
# chrome_driver_path = "C:/Users/taois/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with your ChromeDriver path
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with your Brave browser path

# # Configure options for the WebDriver
# options = Options()
# options.binary_location = brave_path  # Point to Brave's executable
# options.add_argument("--headless")  # Run in headless mode
# service = Service(chrome_driver_path)

# # Initialize WebDriver
# driver = webdriver.Chrome(service=service, options=options)

# # Read CSV file and prepare DataFrame
# data = pd.read_csv('data.csv')
# df = pd.DataFrame(data)
# columns_to_check = ['rating', 'num_reviews', 'description', 'pros', 'cons', 'best_uses', 'describe_yourself']
# urls = df['product_link'][df[columns_to_check].isnull().any(axis=1)]

# collected_data = []

# # Define timeout duration in seconds
# PROCESS_TIMEOUT = 15

# # Function to process a single URL
# def process_url(url):
#     result = {
#         'Item_id': url[-7:],
#         'url': url,
#         'rating': np.nan,
#         'review_count': np.nan,
#         'recommendation_percentage': np.nan,
#         'ratings_distribution': np.nan,
#         'pros': np.nan
#     }
#     try:
#         print(f"Processing URL: {url}")
#         driver.get(url + '#reviews')

#         # Wait for the reviews section to load
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, 'reviewsSnap'))
#         )

#         # Locate the reviews snapshot container
#         try:
#             reviews_snapshot = driver.find_element(By.CLASS_NAME, 'ProductReviews__Reviews--containerSnap')
            
#             # Extract data
#             try:
#                 result['rating'] = reviews_snapshot.find_element(By.CLASS_NAME, 'pr-snippet-rating-decimal').text.strip()
#             except:
#                 pass

#             try:
#                 result['review_count'] = reviews_snapshot.find_element(By.CLASS_NAME, 'pr-snippet-review-count').text.strip()
#             except:
#                 pass

#             try:
#                 result['recommendation_percentage'] = reviews_snapshot.find_element(By.CLASS_NAME, 'pr-reco-value').text.strip()
#             except:
#                 pass

#             # Extract ratings distribution
#             try:
#                 ratings_distribution = []
#                 histogram_items = reviews_snapshot.find_elements(By.CLASS_NAME, 'pr-ratings-histogram-list-item')
#                 for item in histogram_items:
#                     try:
#                         star_rating = item.find_element(By.CLASS_NAME, 'pr-histogram-label').text.strip()
#                         hist_review_count = item.find_element(By.CLASS_NAME, 'pr-histogram-count').text.strip()
#                         ratings_distribution.append(f"{star_rating}: {hist_review_count} reviews")
#                     except:
#                         continue
#                 result['ratings_distribution'] = "; ".join(ratings_distribution)
#                 print(result['ratings_distribution'])
#             except:
#                 pass

#             # Extract pros
#             try:
#                 result['pros'] = "; ".join(
#                     [pro.text.strip() for pro in reviews_snapshot.find_elements(By.TAG_NAME, 'dd') if pro.text.strip()]
#                 )
#                 print(result['pros'])
#             except:
#                 pass

#         except:
#             print(f"Could not find reviews snapshot for URL: {url}")

#     except Exception as e:
#         print(f"Error processing URL {url}: {e}")
#     return result

# # Process URLs with timeout
# for url in urls:
#     try:
#         with ThreadPoolExecutor() as executor:
#             future = executor.submit(process_url, url)
#             collected_data.append(future.result(timeout=PROCESS_TIMEOUT))
#     except TimeoutError:
#         print(f"Timeout occurred for URL: {url}")
#         collected_data.append({
#             'Item_id': url[-7:],
#             'url': url,
#             'rating': np.nan,
#             'review_count': np.nan,
#             'recommendation_percentage': np.nan,
#             'ratings_distribution': np.nan,
#             'pros': np.nan
#         })

# # Save collected data to CSV
# final_df = pd.DataFrame(collected_data)
# final_df.to_csv('product_reviews_pure_selenium_with_timeout.csv', index=False)

# # Close the browser
# driver.quit()
