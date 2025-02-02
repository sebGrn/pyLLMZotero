from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import SystemMessage, HumanMessage

import json
import re

OLLAMA_BASE_URL = "http://127.0.0.1:11434"
OLLAMA_MODEL = "deepseek-r1:7b"

def get_llm():
    llm = ChatOllama(
        temperature=0,  # Use a more deterministic configuration with a low temperature
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        top_k=10,       # A higher value (100) will give more diverse answers, while a lower value (10) will be more conservative.
        top_p=0.5,      # Higher value (0.95) will lead to more diverse text, while a lower value (0.5) will generate more focused text
        num_ctx=3072,   # Sets the size of the context window used to generate the next token.
    )
    return llm

def extract_json(text):
    # Use regex to extract JSON block
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        json_str = json_match.group(0)  # Extract JSON string
        try:
            json_data = json.loads(json_str)  # Convert to dictionary
            return json_data
        except json.JSONDecodeError as e:
            print("Invalid JSON:", e)
            return None
    else:
        print("No JSON found in text.")
        return None
    
def ask_llm_for_keywords(llm, text):
    prompt_template = """You are a helpfull assistant that provides keywords from an abstrat.
        The output is the list of five keywords maximum extracted from the text in a json format only
        Do not provide some explanation or any other information in the output.
        You just have to provide the list of the five keywords in json format

        example:
        input: "This paper presents a path towards the implementation of a Digital Twin for campus environments. 
        The main purpose of the Digital Twin is to accomplish an advanced analytical tool, which supports building owners, 
        uilding operators and building users to reach an improved performance of the building. 
        Digital Twins is new to the building and the real estate industry, hence research within this field is scarce. 
        This paper contributes to the research by providing a methodology to implement a Digital Twin of an existing building stock of campus areas in Sweden. 
        The main results obtained so far are presented. 
        They indicate that the potential of a Digital Twin expands beyond the aspects of a navigational digital 3D model, including a state-of-the-art app that is developed from the Digital Twin platform"
    
        asnwer:
        {
            "keywords": ["Digital Twin", "campus environments", "building owners", "building operators", "building users"]
        }
        """
    messages = [
        SystemMessage(content=prompt_template), 
        HumanMessage(content=text)
        ]
    
    chain = llm | StrOutputParser()
    json_keywords = chain.invoke(messages)
    json_data = extract_json(json_keywords)
    #print(json.dumps(json_data, indent=4))
    return json_data["keywords"]
