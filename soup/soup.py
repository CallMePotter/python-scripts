from bs4 import BeautifulSoup
import requests

source = requests.get("https://wanderinginn.com/table-of-contents").text
soup = BeautifulSoup(source, "html.parser")

links = ""
formatted_text = ""
i = 1
items = {}

for link in soup.find_all("a"):
    links += str(link.text) + "\n"

links = links.splitlines()[24:]

for link in links:
    print("[{}] - {}".format(i, link))
    items[i] = link
    i += 1

chapter = int(input("Enter index to start reading: "))

for link in soup.find_all("a"):
    if items[chapter] == link.text:
        name = link.text
        subsource = requests.get(link.get("href")).text
        subsoup = BeautifulSoup(subsource, "html.parser")

text = subsoup.find("div", {"class": "entry-content"})

for paragraph in text.find_all("p"):
    formatted_text += str(paragraph.text) + "\n"

print(name + "\n")

for line in formatted_text.splitlines()[:-2]:
    print(line)
