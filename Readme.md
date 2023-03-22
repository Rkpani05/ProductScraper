# **Product Scraper**

Product Scraper is a Python script that allows you to scrape product details from Amazon and extract information such as the product URL, name, price, rating, number of reviews, description, ASIN, and manufacturer. The data is then saved in a CSV file.

## Requirements

* Python 3
* requests
* BeautifulSoup

## Installation

* Clone this repository or download the *product_scraper.py file.*

### Install the required packages using pip:

* pip install requests
* pip install beautifulsoup4

## Usage

### Run the script in a Python environment:
* python product_scraper.py

The script will generate two CSV files - *products.csv* and *final_products.csv*. *products.csv* contains the basic product details scraped from the Amazon search result page, and *final_products.csv* contains the additional details scraped from each product page.

## Customization

* To scrape product details from a different website, replace the base_url variable in the code with the URL of the desired website.
* To scrape a different category of products, replace the search term in the base_url variable with the desired category.
* To scrape more or less than 20 pages, change the num_pages variable to the desired number.

## Note

This script is for educational purposes only. The use of automated tools to scrape websites may be against the website's terms of service. Use at your own risk.

## Disclaimer

The information provided by this script is for general informational purposes only. The developer of this script makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the script or the information, products, services, or related graphics contained in the script for any purpose. Any reliance you place on such information is therefore strictly at your own risk.
