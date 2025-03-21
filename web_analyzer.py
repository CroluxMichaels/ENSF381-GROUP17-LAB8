import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

print(soup.prettify())

headings = len(soup.find_all('h1')) + len(soup.find_all('h2')) + len(soup.find_all('h3')) + len(soup.find_all('h4')) + len(soup.find_all('h5')) + len(soup.find_all('h6'))
links = len(soup.find_all('a'))
paragraphs = len(soup.find_all('p'))
print("Number of headings:", headings)
print("Number of links:", links)
print("Number of paragraphs:", paragraphs)

key = input("Please enter a keyword to search for on the Webpage: ").lower()
page = soup.get_text().lower()
words = re.findall(r'\b\w+\b', page)
count = 0
for i in words:
    if i == key: # Ask about this
        count+= 1
print("Number of occurrences:", count)

dict = {}
for i in words:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1


words = ['a', 'b', 'c', 'd', 'e'] # Placeholders
counts = [0, 0, 0, 0, 0] # Placeholders

for key, value in dict.items():
    for i in range(5):
        if value >= counts[i]:
            counts.pop()
            counts.insert(i, value)
            words.pop()
            words.insert(i, key)
            break
print("\nMost common words in the webpage:")
for i in range(5):
    print(f"{words[i]}: {counts[i]} times")

webpage = soup.get_text().split("\n")
max = ""
for i in webpage:
    if len(i) > len(max):
        max = i
print(f"Longest paragraph: {max}")

import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group 17')
plt.ylabel('Count')
plt.show()
            
    

