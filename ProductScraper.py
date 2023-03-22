import csv
import requests
from bs4 import BeautifulSoup

# URL of the website to be scraped
base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'

# Number of pages to scrape
num_pages = 20

# Part - A
# List to store the data
data = []

# Loop through each page and scrape the required data
for i in range(1, num_pages+1):
    url = base_url.format(i)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product blocks on the page
    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    # Loop through each product and extract the required details
    for product in products:
        product_url = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal'})['href']
        product_name = product.find('h2').text.strip()
        product_price = product.find('span', {'class': 'a-price-whole'}).text.strip()

        # Check if rating is available
        rating = product.find('span', {'class': 'a-icon-alt'})
        if rating is not None:
            rating = rating.text.split()[0]
        else:
            rating = ''

        # Check if number of reviews is available
        num_reviews = product.find('span', {'class': 'a-size-base'})
        if num_reviews is not None:
            num_reviews = num_reviews.text.strip()
        else:
            num_reviews = ''
            
        # Append the extracted data to the list
        data.append([product_url, product_name, product_price, rating, num_reviews])

# Save the data to a CSV file
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews'])
    writer.writerows(data)

#Part B

final_data = []

for item in data:
    product_url = item[0]
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting the required fields
    description_elem = soup.find('div', {'id': 'productDescription'})
# Find ASINdescription_elem = soup.find('div', {'id': 'productDescription'})
    if description_elem:
        description = description_elem.text.strip()
    else:
        description = ''
    asin_elem = soup.find('th', text='ASIN')
    if asin_elem:
        asin = asin_elem.parent.td.text.strip()
    else:
        asin = ''
    product_desc_elem = soup.find('div', {'id': 'featurebullets_feature_div'})
    if product_desc_elem:
        product_desc = product_desc_elem.ul.text.strip()
    else:
        product_desc = ''

    
    description = soup.find('div', {'id': 'productDescription'})
    if description is not None:
        description = description.text.strip()
    else:
        description = ''
    
    # Extracting the manufacturer
    manufacturer = soup.find('a', {'id': 'bylineInfo'})
    if manufacturer is not None:
        manufacturer = manufacturer.text.strip()
    else:
        manufacturer = ''

    # Appending the extracted data to the final list
    final_data.append(item + [description, asin, product_desc, manufacturer])

# Saving the final data to a CSV file
with open('final_products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews', 'Description', 'ASIN', 'Product Description', 'Manufacturer'])
    writer.writerows(final_data)
