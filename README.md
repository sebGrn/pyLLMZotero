# llmZotero

## **📌Purpose of the Code:**

This script is designed to  **retrieve research papers from Zotero, extract keywords using an LLM (Large Language Model), and store the processed data into a Neo4j graph database** .

* 📚 **Extracts research papers from Zotero**
* 🧠 **Uses LLM to generate keywords from abstracts**
* 📊 **Stores processed data in a CSV file**
* 🌐 **Inserts paper metadata into a Neo4j graph database**

## **🚀 Why This Code is Useful?**

- ✅ **Automates Zotero data extraction** → No manual export needed.
- ✅ **Uses AI (LLM) to generate keywords** → Helps in better search & organization.
- ✅ **Stores the data in Neo4j** → Enables **graph-based** academic research analysis.
- ✅ **Reusable & scalable** → Works for large datasets, and the CSV export allows easy debugging.

## **🔥 How to run? **

* `pip install -r requirements.txt`
* This code is based on [Pyzotero: a Python client for the Zotero API](https://github.com/urschrei/pyzotero?tab=readme-ov-file) and [LangChain](https://www.langchain.com/)
* You must have a local neo4j server with a db called `neo4j`, the password must be stored as an environment variable called "`NEO4J_ZOTERO_PASSWORD`
* You'll also need **Zotero API key** ([Zotero | API key](https://www.zotero.org/settings/keys/new)) that must be stored in as an environment variable called `ZOTERO_API_KEY`
* And a personal **Zotero library ID** ([Zotero | Library Id](https://www.zotero.org/settings/security#applications)), it must be stored in as an environment variable called `ZOTERO_LIB_ID`
* You need **Ollama server** running locally with `deepseek-r1 `model downloaded. For that go to [Ollama](https://ollama.com/) and install the server locally, then type `ollama pull deepseek-r1:7b` to dowload the llm model locally
