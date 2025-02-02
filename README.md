# llmZotero

## **📌Purpose of the Code:**

This script is designed to  **retrieve research papers from Zotero, extract keywords using an LLM (Large Language Model), and store the processed data into a Neo4j graph database** .

* 📚 **Extracts research papers from Zotero**
* 🧠 **Uses LLM to generate keywords from abstracts**
* 📊 **Stores processed data in a CSV file**
* 🌐 **Inserts paper metadata into a Neo4j graph database**

## **🚀 Why This Code is Useful?**

✅ **Automates Zotero data extraction** → No manual export needed.
✅ **Uses AI (LLM) to generate keywords** → Helps in better search & organization.
✅ **Stores the data in Neo4j** → Enables **graph-based** academic research analysis.
✅ **Reusable & scalable** → Works for large datasets, and the CSV export allows easy debugging.

## How to run

* `pip install -r requirements.txt`
* This code is based on [Pyzotero: a Python client for the Zotero API](https://github.com/urschrei/pyzotero?tab=readme-ov-file) and [LangChain](https://www.langchain.com/)
* You must have a local neo4j server with a db called `neo4j`, password must be stored as an environment variable called "`NEO4J_ZOTERO_PASSWORD`
* You'll also need **Zotero API key** ([Zotero | API key](https://www.zotero.org/settings/keys/new)) that must be stored in as an environment variable called `ZOTERO_API_KEY`
* And a personal **Zotero library ID** ([Zotero | Library Id](https://www.zotero.org/settings/security#applications)), it must be stored in as an environment variable called `ZOTERO_LIB_ID`
* You need **Ollama server** running locally with `deepseek-r1 `model downloaded. For that go to [Ollama](https://ollama.com/) and install the server locally, then type `ollama pull deepseek-r1:7b` to dowload the llm model locally

## Possible Next Features & Enhancements

### **Enhance Keyword Extraction**

🔹 **Problem:** The current LLM extracts keywords but doesn't rank them by importance.
🔹 **Solution:**

* Use **TF-IDF** (Term Frequency-Inverse Document Frequency) to prioritize relevant keywords.
* Implement **Named Entity Recognition (NER)** to detect  **authors, institutions, topics, and locations** .

### **Semantic Search with LLM & Vector Database**

🔹 **Problem:** Finding related papers currently relies on  **Neo4j relationships** .
🔹 **Solution:**

* **Embed abstracts using an LLM** (e.g., OpenAI, Sentence Transformers).
* **Store embeddings in a vector database** (e.g., Weaviate, FAISS, or Neo4j vector indexing).
* **Enable similarity search** (find papers on similar topics).

### **Automated Research Summarization & Topic Clustering**

🔹 **Problem:** Hard to quickly understand research trends from papers.
🔹 **Solution:**

* **Summarize abstracts** using `GPT` or `BART` to create a short 3-line summary.
* **Cluster similar papers** into research topics using `K-Means` or `Hierarchical Clustering`.

### **Automated Citations & Cross-References in Neo4j**

🔹 **Problem:** Zotero provides citations but doesn’t connect papers  **by citation relationships** .
🔹 **Solution:**

* Extract **cited references** from each paper.
* Create **CITATION** relationships in Neo4j.
* Use Neo4j queries to find **most-cited papers**

### **Author Network & Collaboration Graph**

🔹 **Problem:** No insight into author collaborations.
🔹 **Solution:**

* Extract **authors** from Zotero.
* Create **COAUTHOR relationships** in Neo4j.
* Visualize  **collaboration networks** .
