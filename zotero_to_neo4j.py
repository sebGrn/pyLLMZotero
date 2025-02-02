# %%
from src.neo4j_exporter import neo4j_connector, neo4j_exporter
from src.zotero_exporter import zotero_connector, get_items, process_items
from src.llm_for_zotero import get_llm, ask_llm_for_keywords

# %%
zotero_connector = zotero_connector()
items = get_items(zotero_connector)
papers_df = process_items(items)
print(papers_df.head())

# %%
llm = get_llm()
keywords = []
# loop on df
for index, row in papers_df.iterrows():
    text = row.abstract
    if len(text) == 0:
        keywords.append([])
    else:
        keywords.append(ask_llm_for_keywords(llm, text))

papers_df['keywords'] = keywords
print(papers_df.head())

# %%
papers_df.to_csv('./papers.csv', index=False)

# %%
driver = neo4j_connector()
neo4j_exporter(driver, papers_df.to_dict('records'))