from bs4 import BeautifulSoup
with open("TEPKA - 7TV.html", "r", encoding="utf-8") as file:
    html = file.read()

soup=BeautifulSoup(html, 'html.parser')
name = [span.text for span in soup.find_all("span", class_="name svelte-clww9e")]
print(*name, sep='\n')

with open("emotes.txt", "w", encoding="utf-8") as file:
    for title in name:
        file.write(title + "\n")