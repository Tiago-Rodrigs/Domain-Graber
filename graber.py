import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the topic
topic = "machine learning"

# Define a list to store the website domains
website_domains = []

# Define the number of pages to scrape
num_pages = 5

# Iterate through the pages
for i in range(num_pages):
    # Send GET request to Google search with the topic and the page number
    response = requests.get(
        f"https://www.google.com/search?q={topic}+wordpress&start={i*20}")
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the website domains
    for link in soup.find_all("a"):
        website_domains.append(link.get("href").split("/")[2])

# Create a DataFrame from the list of website domains
df = pd.DataFrame(website_domains, columns=["domain"])

# Remove duplicate domains
df.drop_duplicates(inplace=True)

# Print the DataFrame
print(df)

print(website_domains)
