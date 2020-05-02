import atoma
import requests

response = requests.get('https://www.heise.de/rss/heise-atom.xml')
feed = atoma.parse_atom_bytes(response.content)
for entry in feed.entries:
    print(entry.published)
    print("******")
    print(entry.summary)
