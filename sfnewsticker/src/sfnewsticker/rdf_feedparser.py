import feedparser

NewsFeed = feedparser.parse("https://www.heise.de/rss/heise.rdf")

for entry in NewsFeed.entries:
    print(entry.published)
    print("******")
    print(entry.summary)
    print("------News Link--------")
    print(entry.link)

