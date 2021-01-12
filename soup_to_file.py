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

for chapter in links:
    for link in soup.find_all("a"):
        if chapter == link.text:
            file = open("inn/" + link.text, "w")
            name = link.text
            subsource = requests.get(link.get("href")).text
            subsoup = BeautifulSoup(subsource, "html.parser")

    text = subsoup.find("div", {"class": "entry-content"})

    try:
        for paragraph in text.find_all("p"):
            formatted_text += str(paragraph.text) + "\n"
    except AttributeError:
        pass

    file.write(name + "\n")

    for line in formatted_text.splitlines()[:-2]:
        file.write(line + "\n")
