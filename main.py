import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import load_dotenv
import os

# Load environment variable from the .env file
load_dotenv("./vars/.env")

"""
Using headers with the python requests library's get method
https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method
"""
YOUR_EMAIL = os.getenv("MY_EMAIL")
YOUR_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

response = requests.get(URL, headers=header)
response.raise_for_status()
amazon_item = response.content


# Parse the LXML content using BeautifulSoup
soup = BeautifulSoup(amazon_item, "lxml")
# print(soup.prettify())

# Extract the price from the site
price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 99

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr="alvinchinuk@gmail.com",
            to_addrs="alvinwen3@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )