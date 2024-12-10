import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import re
import os

# List of URLs (replace with actual URLs or use a CSV)
urls = pd.read_csv('data.csv')
urls = urls['product_link']
numof = len(urls)
nownum = 1

# สร้างโครงสร้าง DataFrame
data = {
    'Item_id': [],
    'syndicated_review_count': [],
    'negative_comments': []
}

# Headers for HTTP requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36'
}

# Iterate over each URL and scrape the corresponding page
for url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=15)

        # Check if the page was successfully retrieved
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Convert the BeautifulSoup object into an lxml tree to support XPath
            tree = html.fromstring(str(soup))

            # Scraping the Item ID (from the URL)
            item_id = url.split("?sku=")[-1]  # Assuming item_id is after "?sku="
            data['Item_id'].append(item_id)

            # Scraping syndicated_review_count using XPath
            xpath_expression = '//*[@id="pr-review-snapshot"]/section[2]/section[2]/p/font[1]/font'  # Replace this with the actual XPath
            syndicated_review_count = tree.xpath(xpath_expression)

            if syndicated_review_count:
                # If found, extract the review count text
                data['syndicated_review_count'].append(syndicated_review_count[0].text.strip())
            else:
                data['syndicated_review_count'].append('nan')

            # Scraping negative_comments from <script>
            script_tag = soup.find('script', id='apollo_state')
            if script_tag:
                script_content = script_tag.string

                # Find negativeComments using Regular Expression
                negative_comment_match = re.search(r'"negativeComments":"(.*?)"', script_content)
                if negative_comment_match:
                    negative_comment = negative_comment_match.group(1)
                    data['negative_comments'].append(negative_comment)
                else:
                    data['negative_comments'].append("No Negative Comment")
            else:
                data['negative_comments'].append("No Script Found")
        else:
            print(f'Failed to retrieve page for {url}. Status Code: {response.status_code}')
            data['Item_id'].append('nan')
            data['syndicated_review_count'].append('nan')
            data['negative_comments'].append('nan')

    except Exception as e:
        print(f"Error processing URL {url}: {e}")
        data['Item_id'].append('nan')
        data['syndicated_review_count'].append('nan')
        data['negative_comments'].append('nan')

    # Print progress and current item
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-' * (len(data['Item_id'][-1]) + 20), '\n',
          '|Item_id =', data['Item_id'][-1], '\n',
          '|syndicated_review_count =', data['syndicated_review_count'][-1], '\n',
          '|negative_comments =', data['negative_comments'][-1], '\n')
    print('-' * (len(data['Item_id'][-1]) + 20))
    print('=' * (int((nownum / numof) * 70) + 1), f'Scrap process now: {round((nownum / numof) * 100, 2)} %')

    nownum += 1

# Save the collected data to a CSV file
data = pd.DataFrame(data)
data.to_csv('combined_scraped_data.csv', index=False, encoding='utf-8-sig')
print("Scraping completed! Data saved to 'combined_scraped_data.csv'")
