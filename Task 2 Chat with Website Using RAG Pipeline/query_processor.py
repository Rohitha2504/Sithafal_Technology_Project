class QueryProcessor:
    def __init__(self, scraped_data):
        self.scraped_data = scraped_data

    def search(self, query):
        results = []
        for record in self.scraped_data:
            title = record['title'].lower()
            content = record['content'].lower()
            if query.lower() in title or query.lower() in content:
                results.append(record)
        return results
