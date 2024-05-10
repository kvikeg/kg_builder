#!/usr/bin/env python3
import os

from langchain_community.graphs import Neo4jGraph
os.environ["NEO4J_URI"] = "neo4j+s://ee3ec572.databases.neo4j.io"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "Is80K46La8CdVQY8ZoUjYE8wWJBu0xeufkJhg_P9BCQ"
# AURA_INSTANCEID=ee3ec572
# AURA_INSTANCENAME=Instance01

# graph = Neo4jGraph()

from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

llm.invoke("Tell me a joke")

llm_transformer = LLMGraphTransformer(llm=llm)

from langchain_core.documents import Document

text = """
Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
She was, in 1906, the first woman to become a professor at the University of Paris.
"""
documents = [Document(page_content=text)]
graph_documents = llm_transformer.convert_to_graph_documents(documents)
print(f"Nodes:{graph_documents[0].nodes}")
print(f"Relationships:{graph_documents[0].relationships}")

