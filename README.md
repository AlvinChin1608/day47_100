# day47_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

----------
# ⚠️ Unresolved Issue:

Due to Amazon's anti-scraping measures, retrieving certain data programmatically is not feasible. Efforts to overcome these challenges are ongoing.

__Temporary Workaround (Attempted):__

The script previously attempted to use a library called fake-useragent to generate random user-agents in the request headers. This approach aimed to mimic real browser behavior and potentially bypass some anti-scraping checks. However, its effectiveness was limited and became unreliable after a short period.

```python
import requests
from bs4 import BeautifulSoup
import fake_useragent
from time import sleep

# Generate a random user-agent
user_agent = fake_useragent.UserAgent().chrome

headers = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent': user_agent
}

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

try:
  response = requests.get(URL, headers=headers)
  response.raise_for_status()
  sleep(2)  # Introduce a short delay
  amazon_item = response.content
  soup = BeautifulSoup(amazon_item, "lxml")

  # Look for the price element based on current HTML structure (adapt if needed)
  price = soup.find(name="span", class_="a-offscreen")
  if price:
      print(price.text)
  else:
      print("Price not found using current approach.")

except requests.exceptions.RequestException as e:
  print(f"Error: {e}")
```

__Future Considerations:__

Continue to investigate alternative methods for data retrieval that respect Amazon's guidelines and adapt to evolving website structures.
https://www.amazon.com/robots.txt
