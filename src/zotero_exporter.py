from pyzotero import zotero
import os
import pandas as pd

def zotero_connector():
    api_key = os.getenv('ZOTERO_API_KEY')
    library_id = os.getenv('ZOTERO_LIB_ID')
    zot = zotero.Zotero(library_id, 'user', api_key)
    return zot

def get_items(zot):
    # Get all items from the library
    print('Getting items from Zotero...')
    items = zot.everything(zot.items())
    return items

def process_items(items):
    print('Processing items...')
    keys, titles, urls, dates, bookTitles, authors, abstracts = [], [], [], [], [], [], []

    # Print details of each item
    for item in items:
        paper = item["data"]        
        if("title" not in paper):
            # Skip items without a title
            continue
        
        keys.append(item["key"])
        titles.append(paper["title"])
        urls.append(paper.get("url", ""))
        dates.append(paper.get("date", ""))
        bookTitles.append(paper.get("bookTitle", ""))
        abstracts.append(paper.get("abstractNote", ""))

        authors_list = []
        if "creators" in paper:
            authors_list.extend(
                author["firstName"] + author["lastName"]
                for author in paper["creators"]
                if author.get("creatorType") == "author" and "firstName" in author and "lastName" in author
            )
        authors.append(authors_list)

    return pd.DataFrame({
        "key": keys,
        "title": titles,
        "url": urls,
        "date": dates,
        "bookTitle": bookTitles,
        "author": authors,
        "abstract": abstracts
    })
