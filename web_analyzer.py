import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

print(soup.prettify())

numheadings = len(soup.find_all('h1')) + len(soup.find_all('h2')) + len(soup.find_all('h3')) + len(soup.find_all('h4')) + len(soup.find_all('h5')) + len(soup.find_all('h6'))
print("Number of headings:", numheadings)
print("Number of links:", len(soup.find_all('a')))
print("Number of paragraphs:", len(soup.find_all('p')))

key = input("Please enter a keyword to search for on the Webpage: ").lower()
page = soup.prettify().lower().split()
count = 0
for i in page:
    if i == key: # Ask about this
        count+= 1
print("Number of occurrences:", count)

content = soup.get_text().split()
dict = {}
for i in content:
    i = i.lower()
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

print(words)
print(counts)

            
    

