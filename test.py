# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from bs4 import BeautifulSoup
# # import pandas as pd

# # # Setup Selenium WebDriver
# # chrome_driver_path = "C:/Users/taois/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with your ChromeDriver path
# # brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with your Brave browser path

# # # Configure options for the WebDriver
# # options = Options()
# # options.binary_location = brave_path  # Point to Brave's executable
# # options.add_argument("--headless")  # Run in headless mode
# # service = Service(chrome_driver_path)
# # driver = webdriver.Chrome(service=service, options=options)

# # # URL to visit
# # # url = "https://www.ulta.com/p/double-wear-stay-in-place-foundation-xlsImpprod14641507?sku=2309420#reviews"  # Replace with the actual URL
# # data = pd.read_csv('data.csv')
# # df = pd.DataFrame(data)
# # columns_to_check = ['rating','num_reviews','description','pros','cons','best_uses','describe_yourself']
# # urls = df['product_link'][df[columns_to_check].isnull().any(axis=1)]
# # try:
# #     dana = {'Item_id':[],'pors':[],'cons':[],'recom':[],'rating':[],'num_reviews':[]}
# #     for url in urls:
# #         driver.get(url+'#reviews')
# #         driver.implicitly_wait(10)  # Allow time for dynamic content to load
        
# #         # Locate the histogram block and get the HTML content
# #         element = driver.find_element(By.CLASS_NAME, "pr-review-snapshot-block-container")
# #         html_content = element.get_attribute("outerHTML")
        
# #         # Use BeautifulSoup to parse the HTML
# #         soup = BeautifulSoup(html_content, "html.parser")
        
# #         # Extract star ratings and counts
# #         ratings = soup.find_all("li", class_="pr-ratings-histogram-list-item")
# #         for rating in ratings:
# #             star_label = rating.find("p", class_="pr-histogram-label").text.strip()
# #             star_count = rating.find("p", class_="pr-histogram-count").text.strip()
# #             print(f"{star_label}: {star_count} reviews")


# #         elementH = driver.find_element(By.XPATH, "//header[@class='pr-review-snapshot-header pr-review-snapshot-content-block']")
# #         html_contentH = elementH.get_attribute("outerHTML")
        

# #         soup = BeautifulSoup(html_content, "html.parser")
# #         soupH = BeautifulSoup(html_contentH, "html.parser")
        
# #         pros_section = soup.find("div", class_="pr-review-snapshot-block-container")

# #         head = soupH.find('header', class_="pr-review-snapshot-header pr-review-snapshot-content-block")

# #         if head:
# #             head = head.find('section', class_="pr-review-snapshot-snippets")
# #             if head:
# #                 head2 = head.find('div', class_="pr-snippet-stars-reco-inline pr-snippet-standard")
# #                 if head2:
# #                     head3 = head2.find('div', class_="pr-snippet-stars-reco-stars")
# #                     if head3:
# #                         head4 = head3.find('div', class_="pr-snippet")
# #                         if head4:
# #                             numre = head4.find('div',class_="pr-snippet-read-and-write")
# #                             head5 = head4.find('div', class_="pr-snippet-stars-container")
# #                             if head5:
# #                                 head6 = head4.find('div', class_="pr-snippet-stars pr-snippet-stars-png")
# #                                 if head6:
# #                                     head7 = head4.find('div', class_="pr-snippet-rating-decimal").get_text()
# #                                     if head7:
# #                                         print('average reviews :',head7)
# #                                         dana['rating'].append(head7)
# #                             if numre:
# #                                 numRe = numre.find('span',class_="pr-snippet-review-count").get_text()
# #                                 print('all review :',numRe)
# #                                 dana['num_reviews'].append(numRe)
# #                 if head2:
# #                     reccom = head2.find('div',class_="pr-snippet-stars-reco-reco")
# #                     if reccom:
# #                         reccom2 = reccom.find('dic',class_="pr-snippet-reco-to-friend")
# #                         if reccom2:
# #                             reccom3 = reccom2.find('div',class_="pr-snippet-reco-to-friend-percent pr-snippet-reco-to-friend-green")
# #                             if reccom3:
# #                                 reccmand = reccom3.find('div',class_="pr-reco pr-reco-green").get_text()
# #                                 print(reccmand)
# #                                 dana['recom'].append(reccmand)


# #         if pros_section:
# #             pros_section = pros_section.find('section', class_="pr-review-snapshot-block pr-review-snapshot-block-pros").find('dl',class_="pr-review-snapshot-tags").find_all('dd',class_="pr-snapshot-tag-def")
# #             # print('Found')
# #         cons_section = soup.find("div", class_="pr-review-snapshot-block-container")

# #         if cons_section:
# #             cons_section = cons_section.find('section', class_="pr-review-snapshot-block pr-review-snapshot-block-cons").find('dl',class_="pr-review-snapshot-tags").find_all('dd',class_="pr-snapshot-tag-def")
# #             # print('Found')
# #         print("PROS:")
# #         for pros in pros_section:
# #             dana['pors'].append(pros.text.strip())
# #             print(pros.text.strip())
        
# #         print("\nCONS:")
# #         for cons in cons_section:
# #             dana['cons'].append(cons.text.strip())
# #             print(cons.text.strip())

# # finally:
# #     driver.quit()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import pandas as pd

# # Setup Selenium WebDriver
# chrome_driver_path = "C:/Users/taois/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with your ChromeDriver path
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with your Brave browser path

# # Configure options for the WebDriver
# options = Options()
# options.binary_location = brave_path  # Point to Brave's executable
# # options.add_argument("--headless")  # Run in headless mode
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# # Read existing data from CSV
# data = pd.read_csv('data.csv')
# df = pd.DataFrame(data)
# columns_to_check = ['rating', 'num_reviews', 'description', 'pros', 'cons', 'best_uses', 'describe_yourself']
# urls = df['product_link'][df[columns_to_check].isnull().any(axis=1)]

# # Prepare the dictionary to store scraped data
# dana = {'Item_id': [], 'pros': [], 'cons': [], 'recom': [], 'rating': [], 'num_reviews': [],
#         '5_stars': [], '4_stars': [], '3_stars': [], '2_stars': [], '1_star': []}

# try:
#     for url in urls:
#         driver.get(url + '#reviews')
#         driver.implicitly_wait(60)  # Allow time for dynamic content to load
        
#         # Locate the histogram block and get the HTML content
#         element = driver.find_element(By.CLASS_NAME, "pr-review-snapshot-block-container")
#         html_content = element.get_attribute("outerHTML")
        
#         # Use BeautifulSoup to parse the HTML
#         soup = BeautifulSoup(html_content, "html.parser")
        
#         # Extract star ratings and counts (the histogram)
#         ratings = soup.find_all("li", class_="pr-ratings-histogram-list-item")
        
#         # Initialize variables for star counts
#         stars_count = {'5_stars': 0, '4_stars': 0, '3_stars': 0, '2_stars': 0, '1_star': 0}
        
#         # Loop through ratings and update the star counts
#         for rating in ratings:
#             star_label = rating.find("p", class_="pr-histogram-label").text.strip()
#             star_count = rating.find("p", class_="pr-histogram-count").text.strip()
#             print('star',star_count)
#             # Map star labels to corresponding columns
#             if "5 Stars" in star_label:
#                 stars_count['5_stars'] = star_count
#             elif "4 Stars" in star_label:
#                 stars_count['4_stars'] = star_count
#             elif "3 Stars" in star_label:
#                 stars_count['3_stars'] = star_count
#             elif "2 Stars" in star_label:
#                 stars_count['2_stars'] = star_count
#             elif "1 Star" in star_label:
#                 stars_count['1_star'] = star_count
        
#         # Store the extracted star counts in the dictionary
#         dana['5_stars'].append(stars_count['5_stars'])
#         dana['4_stars'].append(stars_count['4_stars'])
#         dana['3_stars'].append(stars_count['3_stars'])
#         dana['2_stars'].append(stars_count['2_stars'])
#         dana['1_star'].append(stars_count['1_star'])

#         # Extract other information (pros, cons, rating, etc.)
#         elementH = driver.find_element(By.XPATH, "//header[@class='pr-review-snapshot-header pr-review-snapshot-content-block']")
#         html_contentH = elementH.get_attribute("outerHTML")
#         soupH = BeautifulSoup(html_contentH, "html.parser")

#         pros_section = soup.find("div", class_="pr-review-snapshot-block-container")
#         head = soupH.find('header', class_="pr-review-snapshot-header pr-review-snapshot-content-block")

#         if head:
#             head = head.find('section', class_="pr-review-snapshot-snippets")
#             if head:
#                 head2 = head.find('div', class_="pr-snippet-stars-reco-inline pr-snippet-standard")
#                 if head2:
#                     head3 = head2.find('div', class_="pr-snippet-stars-reco-stars")
#                     if head3:
#                         head4 = head3.find('div', class_="pr-snippet")
#                         if head4:
#                             numre = head4.find('div', class_="pr-snippet-read-and-write")
#                             head5 = head4.find('div', class_="pr-snippet-stars-container")
#                             if head5:
#                                 head6 = head4.find('div', class_="pr-snippet-stars pr-snippet-stars-png")
#                                 if head6:
#                                     head7 = head4.find('div', class_="pr-snippet-rating-decimal").get_text()
#                                     if head7:
#                                         print('average reviews:', head7)
#                                         dana['rating'].append(head7)
#                             if numre:
#                                 numRe = numre.find('span', class_="pr-snippet-review-count").get_text()
#                                 print('all review:', numRe)
#                                 dana['num_reviews'].append(numRe)
#                 if head2:
#                     reccom = head2.find('div', class_="pr-snippet-stars-reco-reco")
#                     if reccom:
#                         reccom2 = reccom.find('dic', class_="pr-snippet-reco-to-friend")
#                         if reccom2:
#                             reccom3 = reccom2.find('div', class_="pr-snippet-reco-to-friend-percent pr-snippet-reco-to-friend-green")
#                             if reccom3:
#                                 reccmand = reccom3.find('div', class_="pr-reco pr-reco-green").get_text()
#                                 print(reccmand)
#                                 dana['recom'].append(reccmand)

#         # Extract pros and cons
#         if pros_section:
#             pros_section = pros_section.find('section', class_="pr-review-snapshot-block pr-review-snapshot-block-pros").find('dl', class_="pr-review-snapshot-tags").find_all('dd', class_="pr-snapshot-tag-def")
#         cons_section = soup.find("div", class_="pr-review-snapshot-block-container")

#         if cons_section:
#             cons_section = cons_section.find('section', class_="pr-review-snapshot-block pr-review-snapshot-block-cons").find('dl', class_="pr-review-snapshot-tags").find_all('dd', class_="pr-snapshot-tag-def")

#         print("PROS:")
#         for pros in pros_section:
#             dana['pros'].append(pros.text.strip())
#             print(pros.text.strip())

#         print("\nCONS:")
#         for cons in cons_section:
#             dana['cons'].append(cons.text.strip())
#             print(cons.text.strip())

# finally:
#     driver.quit()

# # Convert the dictionary to a DataFrame
# df_result = pd.DataFrame(dana)

# # Save the DataFrame to a CSV file
# df_result.to_csv('scraped_reviews.csv', index=False)

# print("Scraping completed. Data saved to 'scraped_reviews.csv'")




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Setup Selenium WebDriver
chrome_driver_path = "C:/Users/unkno/scoop/apps/chromedriver/current/chromedriver.exe"  # Replace with your ChromeDriver path
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Replace with your Brave browser path

# Configure options for the WebDriver
options = Options()
options.binary_location = brave_path  # Point to Brave's executable
# options.add_argument("--headless")  # Run in headless mode
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Read existing data from CSV
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
columns_to_check = ['rating', 'num_reviews', 'description', 'pros', 'cons', 'best_uses', 'describe_yourself']
urls = df['product_link'][df[columns_to_check].isnull().any(axis=1)]

# Prepare the dictionary to store scraped data
dana = {'Item_id': [], 'pros': [],'cons': [], 'rating': [], 'num_reviews': [],
        '5_stars': [], '4_stars': [], '3_stars': [], '2_stars': [], '1_star': []}

try:
    for url in urls:
        driver.get(url + '#reviews')
        driver.implicitly_wait(10)  # Allow time for dynamic content to load
        
        # Check if the page is unavailable (i.e., contains the "We can’t load this page" message)
        try:
            unavailable_message = driver.find_element(By.XPATH, "//div[@class='TextOnlyHero__headline']/h1[contains(text(), 'We can’t load this page')]")
            print(f"Skipping deleted or unavailable page: {url}")
            continue
        except:
            pass  # Continue if the message is not found

        # Locate the histogram block and get the HTML content
        try:
            element = driver.find_element(By.CLASS_NAME, "pr-review-snapshot-block-container")
            html_content = element.get_attribute("outerHTML")
            
            # Use BeautifulSoup to parse the HTML
            soup = BeautifulSoup(html_content, "html.parser")
            
            # Extract star ratings and counts (the histogram)
            ratings = soup.find_all("li", class_="pr-ratings-histogram-list-item")
            
            # Initialize variables for star counts
            stars_count = {'5_stars': 0, '4_stars': 0, '3_stars': 0, '2_stars': 0, '1_star': 0}
            
            # Loop through ratings and update the star counts
            for rating in ratings:
                star_label = rating.find("p", class_="pr-histogram-label").text.strip()
                star_count = rating.find("p", class_="pr-histogram-count").text.strip()
                print('star', star_count)
                # Map star labels to corresponding columns
                if "5 Stars" in star_label:
                    stars_count['5_stars'] = star_count
                elif "4 Stars" in star_label:
                    stars_count['4_stars'] = star_count
                elif "3 Stars" in star_label:
                    stars_count['3_stars'] = star_count
                elif "2 Stars" in star_label:
                    stars_count['2_stars'] = star_count
                elif "1 Star" in star_label:
                    stars_count['1_star'] = star_count
            
            # Store the extracted star counts in the dictionary
            dana['5_stars'].append(stars_count['5_stars'])
            dana['4_stars'].append(stars_count['4_stars'])
            dana['3_stars'].append(stars_count['3_stars'])
            dana['2_stars'].append(stars_count['2_stars'])
            dana['1_star'].append(stars_count['1_star'])
            print(len(dana['5_stars']),len(dana['4_stars']),len(dana['3_stars']),len(dana['2_stars']),len(dana['1_star']))

            # Extract other information (pros, cons, rating, etc.)
            elementH = driver.find_element(By.XPATH, "//header[@class='pr-review-snapshot-header pr-review-snapshot-content-block']")
            html_contentH = elementH.get_attribute("outerHTML")
            soupH = BeautifulSoup(html_contentH, "html.parser")

            pros_section = soup.find("div", class_="pr-review-snapshot-block-container")
            head = soupH.find('header', class_="pr-review-snapshot-header pr-review-snapshot-content-block")

            if head:
                head = head.find('section', class_="pr-review-snapshot-snippets")
                if head:
                    head2 = head.find('div', class_="pr-snippet-stars-reco-inline pr-snippet-standard")
                    if head2:
                        head3 = head2.find('div', class_="pr-snippet-stars-reco-stars")
                        if head3:
                            head4 = head3.find('div', class_="pr-snippet")
                            if head4:
                                numre = head4.find('div', class_="pr-snippet-read-and-write")
                                head5 = head4.find('div', class_="pr-snippet-stars-container")
                                if head5:
                                    head6 = head4.find('div', class_="pr-snippet-stars pr-snippet-stars-png")
                                    if head6:
                                        head7 = head4.find('div', class_="pr-snippet-rating-decimal").get_text()
                                        if head7:
                                            print('average reviews:', head7)
                                            dana['rating'].append(head7)
                                if numre:
                                    numRe = numre.find('span', class_="pr-snippet-review-count").get_text()
                                    print('all review:', numRe)
                                    dana['num_reviews'].append(numRe)
                    if head2:
                        reccom = head2.find('div', class_="pr-snippet-stars-reco-reco")
                        if reccom:
                            reccom2 = reccom.find('dic', class_="pr-snippet-reco-to-friend")
                            if reccom2:
                                reccom3 = reccom2.find('div', class_="pr-snippet-reco-to-friend-percent pr-snippet-reco-to-friend-green")
                                if reccom3:
                                    reccmand = reccom3.find('div', class_="pr-reco pr-reco-green").get_text()
                                    print(reccmand)
                                    dana['recom'].append(reccmand)

            # Extract pros and cons
            if pros_section:
                pros_section = pros_section.find('section', class_="pr-review-snapshot-block pr-review-snapshot-block-pros").find('dl', class_="pr-review-snapshot-tags").find_all('dd', class_="pr-snapshot-tag-def")
            cons_section = soup.find("div", class_="pr-review-snapshot-block-container")

            if cons_section:
                cons_section = cons_section.find('section', class_="pr-review-snapshot-block pr-review-snapshot-block-cons").find('dl', class_="pr-review-snapshot-tags").find_all('dd', class_="pr-snapshot-tag-def")

            print("PROS:")
            d0 = []
            for pros in pros_section:
                print(pros.text.strip())
                d0.append(pros.text.strip())
            dana['pros'].append(d0)

            print("\nCONS:")
            d1 = []
            for cons in cons_section:
                print(cons.text.strip())
                d1.append(cons.text.strip())
            dana['cons'].append(d1)

            print(url[-7:])
            dana['Item_id'].append(url[-7:])
            print('__________________________________________')
            
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            continue  # Skip to the next URL if there's an error
        # print(dana)
        for i in dana:
            print(len(dana[i]))
        df_result = pd.DataFrame(dana)
        df_result.to_csv('scraped_reviews.csv')


finally:
    driver.quit()

# Convert the dictionary to a DataFrame
df_result = pd.DataFrame(dana)
df_result.to_csv('scraped_reviews.csv')
print("Scraping completed. Data saved to 'scraped_reviews.csv'")
# for i in df_result.columns:
#     print(len(df_result[i]))
