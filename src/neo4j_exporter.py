from neo4j import GraphDatabase
import os
import pandas as pd

def neo4j_connector():
    host = 'bolt://localhost:7687'
    user = 'neo4j'
    password = os.getenv('NEO4J_ZOTERO_PASSWORD')
    driver = GraphDatabase.driver(host,auth=(user, password))
    return driver

def run_query(driver, query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        return pd.DataFrame([r.values() for r in result], columns=result.keys())

def neo4j_exporter(driver, paper_list):
    '''
    Export data to Neo4j as a graph
    paper_list: list of dictionaries
    '''

    # remove previous graph
    run_query(driver, "MATCH (n) DETACH DELETE n")

    # all name from articles are unique
    run_query(driver, "CREATE CONSTRAINT IF NOT EXISTS ON (a:Author) ASSERT a.name IS UNIQUE;")
    run_query(driver, "CREATE CONSTRAINT IF NOT EXISTS ON (a:Article) ASSERT a.key IS UNIQUE;")

    import_query = """
        UNWIND $data AS row
        // Store article
        MERGE (a:Article {key: row.key, title: row.title, url: row.url, date: row.date, key: row.key, bookTitle: row.bookTitle, abstract: row.abstract, keywords: row.keywords})

        FOREACH (author IN row.author  |
            MERGE (au:Author {name: author})
            MERGE (a)<-[:AUTHORED]-(au))
        """

    r = run_query(driver, import_query, {'data':paper_list})
    return r
